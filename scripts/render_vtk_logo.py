# /// script
# dependencies = [
#   "vtk==9.7.1",
#   "opencv-python-headless",
#   "pillow",
#   "numpy",
#   "imageio-ffmpeg"
# ]
# ///
"""Render the animated 3D VTK logo used in the website hero.

The flat logo is traced into polygons, extruded into 3D letters, and animated:
glass letter shells fill with blue "liquid" one by one while the camera swings
around to a near-front view.

Usage:
    uv run scripts/render_vtk_logo.py LOGO_PNG OUTPUT [OUTPUT ...]

Each OUTPUT's extension picks its format:
    .gif   white background
    .mp4   H.264 "stacked alpha": color on top, alpha as grayscale below.
           Plays everywhere; the site's HeroAnimation recombines the halves
           in WebGL. (VP9 WebM with alpha would be simpler, but Safari
           drops its alpha.)

Alongside the last output, `<name>_final.png`, `<name>_mid.png` and
`<name>_f30.png` stills are written for previews and the poster image.
"""
import math
import os
import subprocess
import sys
import tempfile

import cv2
import numpy as np
import vtk
from PIL import Image
from vtk.util.numpy_support import vtk_to_numpy

# Colors from the official logo.
LOGO_BLUE = (6 / 255, 79 / 255, 141 / 255)
LOGO_GRAY = (147 / 255, 149 / 255, 152 / 255)
GLASS_COLOR = (0.93, 0.95, 0.98)
#GLASS_EDGE_COLOR = (0.45, 0.58, 0.72)
GLASS_EDGE_COLOR = (1.0, 1.0, 1.0)

# Geometry, in logo-image pixels.
LETTER_DEPTH = 90
SHADOW_NEAR_Z, SHADOW_FAR_Z = -70, -30
GLASS_MARGIN = 2  # how far the glass shell stands off the letter faces

RENDER_WIDTH, RENDER_HEIGHT = 1200, 644

# Animation timing.
FRAME_COUNT = 110
FPS = 25
FIRST_FRAME_HOLD_MS = 400
LAST_FRAME_HOLD_MS = 1800

MP4_ENCODER_ARGS = ['-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p',
                    '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-movflags', '+faststart']
# H.264 compresses in 16-pixel blocks; padding each half to a multiple of 16 keeps
# color and alpha from bleeding into each other across the seam.
STACKED_HALF_ALIGNMENT = 16


def load_logo_masks(path):
    """Split the logo image into blue (letters) and gray (shadow strokes) masks."""
    pixels = np.array(Image.open(path).convert('RGBA')).astype(int)
    red, blue, alpha = pixels[..., 0], pixels[..., 2], pixels[..., 3]
    opaque = alpha > 128
    blue_mask = (opaque & (blue > red + 40)).astype(np.uint8) * 255
    gray_mask = (opaque & (abs(red - blue) < 30) & (red > 100) & (red < 200)).astype(np.uint8) * 255
    height, width = pixels.shape[:2]
    return blue_mask, gray_mask, width, height


def trace_outlines(mask, min_area=300):
    """Return simplified outer outlines of every shape in the mask that isn't noise."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return [cv2.approxPolyDP(contour, 1.2, True)[:, 0, :]
            for contour in contours if cv2.contourArea(contour) >= min_area]


def left_to_right(outlines):
    return sorted(outlines, key=lambda outline: outline[:, 0].mean())


def extrude_outline(outline, image_width, image_height, near_z, far_z):
    """Extrude a 2D image-space outline into a closed, triangulated solid."""
    points = vtk.vtkPoints()
    polygon = vtk.vtkPolygon()
    for index, (x, y) in enumerate(outline):
        # Center on the image and flip y so the logo is upright.
        points.InsertNextPoint(x - image_width / 2, image_height / 2 - y, near_z)
        polygon.GetPointIds().InsertNextId(index)
    cells = vtk.vtkCellArray()
    cells.InsertNextCell(polygon)
    face = vtk.vtkPolyData()
    face.SetPoints(points)
    face.SetPolys(cells)

    triangulate_face = vtk.vtkTriangleFilter()
    triangulate_face.SetInputData(face)
    extrude = vtk.vtkLinearExtrusionFilter()
    extrude.SetInputConnection(triangulate_face.GetOutputPort())
    extrude.SetExtrusionTypeToVectorExtrusion()
    extrude.SetVector(0, 0, far_z - near_z)
    extrude.CappingOn()
    clean = vtk.vtkCleanPolyData()
    clean.SetInputConnection(extrude.GetOutputPort())
    triangulate_solid = vtk.vtkTriangleFilter()
    triangulate_solid.SetInputConnection(clean.GetOutputPort())
    triangulate_solid.Update()
    return triangulate_solid.GetOutput()


def add_surface_actor(renderer, solid, color, opacity=1.0, ambient=0.35, diffuse=0.7, specular=0.15):
    """Add a flat-shaded actor for a solid, with normals split at sharp edges."""
    normals = vtk.vtkPolyDataNormals()
    normals.SetInputData(solid)
    normals.SetFeatureAngle(30)
    normals.SplittingOn()
    normals.Update()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(normals.GetOutput())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    surface = actor.GetProperty()
    surface.SetColor(color)
    surface.SetOpacity(opacity)
    surface.SetAmbient(ambient)
    surface.SetDiffuse(diffuse)
    surface.SetSpecular(specular)
    surface.SetSpecularPower(30)
    surface.SetInterpolationToFlat()
    renderer.AddActor(actor)
    return actor


def add_edge_actor(renderer, solid):
    """Add an unlit wireframe of the solid's sharp edges."""
    edges = vtk.vtkFeatureEdges()
    edges.SetInputData(solid)
    edges.BoundaryEdgesOff()
    edges.FeatureEdgesOn()
    edges.SetFeatureAngle(30)
    edges.ManifoldEdgesOff()
    edges.NonManifoldEdgesOff()
    edges.ColoringOff()
    edges.Update()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(edges.GetOutput())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    line = actor.GetProperty()
    line.SetColor(GLASS_EDGE_COLOR)
    line.SetLineWidth(4)
    line.LightingOff()
    line.SetOpacity(0.9)
    renderer.AddActor(actor)
    return actor


def add_liquid_fill(renderer, letter):
    """Add the blue letter clipped by a movable plane, so it can fill up like liquid.

    Returns the clipping plane, the actor, and the letter's bottom and top y.
    """
    clip_plane = vtk.vtkPlane()
    clip_planes = vtk.vtkPlaneCollection()
    clip_planes.AddItem(clip_plane)
    clip = vtk.vtkClipClosedSurface()
    clip.SetInputData(letter)
    clip.SetClippingPlanes(clip_planes)
    normals = vtk.vtkPolyDataNormals()
    normals.SetInputConnection(clip.GetOutputPort())
    normals.SetFeatureAngle(30)
    normals.SplittingOn()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(normals.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    surface = actor.GetProperty()
    surface.SetColor(LOGO_BLUE)
    surface.SetAmbient(0.55)
    surface.SetDiffuse(0.55)
    surface.SetSpecular(0.25)
    surface.SetSpecularPower(40)
    surface.SetInterpolationToFlat()
    renderer.AddActor(actor)
    bounds = letter.GetBounds()
    return clip_plane, actor, bounds[2], bounds[3]


def add_lights(renderer):
    renderer.RemoveAllLights()
    for position, intensity in [((-0.6, 0.8, 1.2), 0.75), ((0.8, 0.2, 1.0), 0.45), ((0, -0.5, 0.6), 0.2)]:
        light = vtk.vtkLight()
        light.SetLightTypeToCameraLight()
        light.SetPosition(*position)
        light.SetFocalPoint(0, 0, 0)
        light.SetIntensity(intensity)
        renderer.AddLight(light)


def smoothstep(t):
    t = min(max(t, 0), 1)
    return t * t * (3 - 2 * t)


def capture_frame(window):
    """Read the window as a premultiplied-alpha image, trimmed to its visible pixels.

    Rendering over a transparent black background leaves the framebuffer
    premultiplied. Trimming each frame keeps memory bounded at large render sizes.
    Returns the trimmed image and its (left, top, right, bottom) box in the window.
    """
    grab = vtk.vtkWindowToImageFilter()
    grab.SetInput(window)
    grab.SetInputBufferTypeToRGBA()
    grab.ReadFrontBufferOff()
    grab.Update()
    rgba = vtk_to_numpy(grab.GetOutput().GetPointData().GetScalars())
    rgba = rgba.reshape(RENDER_HEIGHT, RENDER_WIDTH, -1)[::-1]  # VTK rows are bottom-up
    image = Image.fromarray(rgba.copy(), 'RGBa')
    #box = image.getchannel('a').getbbox() or (0, 0, 1, 1)
    #return image.crop(box), box
    return image


def render_frames(blue_mask, gray_mask, logo_width, logo_height):
    """Build the scene and render every animation frame."""
    def extrude(outline, near_z, far_z):
        return extrude_outline(outline, logo_width, logo_height, near_z, far_z)

    letter_outlines = left_to_right(trace_outlines(blue_mask))
    shadow_outlines = trace_outlines(gray_mask)
    print(len(letter_outlines), 'blue', len(shadow_outlines), 'gray')
    # The glass shells trace a slightly grown mask so they enclose the letters.
    grown_blue_mask = cv2.dilate(blue_mask, np.ones((5, 5), np.uint8))
    glass_outlines = left_to_right(trace_outlines(grown_blue_mask))

    letters = [extrude(outline, 0, LETTER_DEPTH) for outline in letter_outlines]
    glass_shells = [extrude(outline, -GLASS_MARGIN, LETTER_DEPTH + GLASS_MARGIN) for outline in glass_outlines]
    shadows = [extrude(outline, SHADOW_NEAR_Z, SHADOW_FAR_Z) for outline in shadow_outlines]

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0, 0, 0)
    renderer.SetBackgroundAlpha(0)
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.AddRenderer(renderer)
    window.SetSize(RENDER_WIDTH, RENDER_HEIGHT)
    renderer.SetUseDepthPeeling(1)
    renderer.SetMaximumNumberOfPeels(8)
    window.SetAlphaBitPlanes(1)
    window.SetMultiSamples(8)
    renderer.UseFXAAOn()

    for shadow in shadows:
        add_surface_actor(renderer, shadow, LOGO_GRAY, opacity=1.0, ambient=0.45, diffuse=0.6, specular=0.05)
    glass_actors = []
    for shell in glass_shells:
        glass_surface = add_surface_actor(renderer, shell, GLASS_COLOR, opacity=0.35, ambient=0.5, diffuse=0.5, specular=0.4)
        glass_edges = add_edge_actor(renderer, shell)
        glass_actors.append((glass_surface, glass_edges))
    liquid_fills = [add_liquid_fill(renderer, letter) for letter in letters]
    add_lights(renderer)

    camera = renderer.GetActiveCamera()
    camera.SetViewAngle(24)
    frames = []
    for frame_index in range(FRAME_COUNT):
        time = frame_index / FRAME_COUNT
        for letter_index, (clip_plane, liquid, bottom_y, top_y) in enumerate(liquid_fills):
            # Letters start filling one after another and overlap in time.
            fill_start = 0.08 + letter_index * 0.14
            fill_end = fill_start + 0.36
            fill = smoothstep((time - fill_start) / (fill_end - fill_start))
            liquid_level = bottom_y - 5 + (top_y - bottom_y + 10) * fill
            # Tilt the surface while filling, settling flat once full.
            slosh = 0.12 * math.sin(frame_index * 0.45 + letter_index * 1.7) * (1 - fill) * (fill > 0)
            clip_plane.SetOrigin(0, liquid_level, LETTER_DEPTH / 2)
            clip_plane.SetNormal(slosh, -1, 0.0)
            liquid.SetVisibility(fill > 0.001)

            # Fade out the glass once its letter is full.
            glass_fade = smoothstep((time - fill_end) / 0.12)
            glass_surface, glass_edges = glass_actors[letter_index]
            glass_surface.GetProperty().SetOpacity(0.35 * (1 - glass_fade))
            glass_edges.GetProperty().SetOpacity(0.9 * (1 - glass_fade))
            glass_surface.SetVisibility(glass_fade < 0.99)
            glass_edges.SetVisibility(glass_fade < 0.99)

        # Swing the camera in from an angle and settle near the front.
        swing = 1.0 - smoothstep(time / 0.5)
        camera.SetFocalPoint(-20, 0, 10)
        camera.SetPosition(0, 0, 1800)
        camera.SetViewUp(0, 1, 0)
        camera.Azimuth(-40 * swing)
        camera.Elevation(16 * swing)
        camera.OrthogonalizeViewUp()
        renderer.ResetCameraClippingRange()
        window.Render()
        frames.append(capture_frame(window))
    return frames


def save_gif(frames, path):
    on_white = [Image.alpha_composite(Image.new('RGBA', frame.size, 'white'), frame.convert('RGBA')).convert('RGB')
                for frame in frames]
    durations = [1000 // FPS] * len(frames)
    durations[0] = FIRST_FRAME_HOLD_MS
    durations[-1] = LAST_FRAME_HOLD_MS
    paletted = [frame.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE) for frame in on_white]
    paletted[0].save(path, save_all=True, append_images=paletted[1:], duration=durations,
                     loop=0, optimize=True, disposal=1)


def stack_color_and_alpha(frame):
    """Lay out a premultiplied RGBa frame as opaque RGB: color above, alpha below.

    Color stays premultiplied (black where transparent), so compression noise in
    empty areas stays dark instead of fringing the edges.
    """
    premultiplied = np.asarray(frame)
    height, width = premultiplied.shape[:2]
    half_height = -(-height // STACKED_HALF_ALIGNMENT) * STACKED_HALF_ALIGNMENT
    stacked = np.zeros((2 * half_height, width, 3), np.uint8)
    stacked[:height] = premultiplied[..., :3]
    stacked[half_height:half_height + height] = premultiplied[..., 3:4]
    return Image.fromarray(stacked, 'RGB')


def write_video_frames(frames, directory):
    """Write numbered PNGs for ffmpeg, repeating the first and last frames to hold them."""
    sequence = ([frames[0]] * (FIRST_FRAME_HOLD_MS * FPS // 1000)
                + frames[1:-1]
                + [frames[-1]] * (LAST_FRAME_HOLD_MS * FPS // 1000))
    for index, frame in enumerate(sequence):
        frame.convert('RGBA').save(f'{directory}/f{index:04d}.png')


def encode_video(frame_directory, path, encoder_args):
    import imageio_ffmpeg
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error',
                    '-framerate', str(FPS), '-i', f'{frame_directory}/f%04d.png',
                    *encoder_args, path], check=True)


def main():
    logo_path, output_paths = sys.argv[1], sys.argv[2:]
    blue_mask, gray_mask, logo_width, logo_height = load_logo_masks(logo_path)

    frames = render_frames(blue_mask, gray_mask, logo_width, logo_height)
    stacked_frame_directory = None
    for output_path in output_paths:
        extension = os.path.splitext(output_path)[1]
        if extension == '.gif':
            save_gif(frames, output_path)
        elif extension == '.mp4':
            if stacked_frame_directory is None:
                stacked_frame_directory = tempfile.TemporaryDirectory()
                write_video_frames([stack_color_and_alpha(frame) for frame in frames], stacked_frame_directory.name)
            encode_video(stacked_frame_directory.name, output_path, MP4_ENCODER_ARGS)
        else:
            sys.exit(f'unsupported output: {output_path}')

    if len(output_paths):
        stills_base = os.path.splitext(output_paths[-1])[0]
        for name, frame in [('final', frames[-1]), ('mid', frames[FRAME_COUNT // 2]), ('f30', frames[30])]:
            frame.convert('RGBA').save(f'{stills_base}_{name}.png')


if __name__ == '__main__':
    main()
