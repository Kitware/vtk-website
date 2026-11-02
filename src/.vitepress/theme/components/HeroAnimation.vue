<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'

// The video is "stacked alpha" (see scripts/render_vtk_logo.py): premultiplied
// color in the top half, alpha as grayscale in the bottom half, each half padded
// to a multiple of 16 rows. A shader recombines them so the animation is
// transparent in every browser, including Safari, which drops WebM alpha.
// The poster PNG shows until the first frame is drawn, and stays for
// reduced-motion users and browsers without WebGL.
const WIDTH = 1200
const HEIGHT = 644 // content rows per half; must match RENDER_HEIGHT in the script

const VERTEX_SHADER = `
attribute vec2 position;
varying vec2 uv;
void main() {
  uv = vec2(position.x * 0.5 + 0.5, 0.5 - position.y * 0.5);
  gl_Position = vec4(position, 0.0, 1.0);
}`

const FRAGMENT_SHADER = `
precision mediump float;
uniform sampler2D frame;
uniform float contentHeight; // HEIGHT as a fraction of the full video height
varying vec2 uv;
void main() {
  vec3 color = texture2D(frame, vec2(uv.x, uv.y * contentHeight)).rgb;
  float alpha = texture2D(frame, vec2(uv.x, 0.5 + uv.y * contentHeight)).r;
  // Premultiplied output; clamp so compression noise can't make color exceed alpha.
  gl_FragColor = vec4(min(color, vec3(alpha)), alpha);
}`

const canvas = ref<HTMLCanvasElement>()
const video = ref<HTMLVideoElement>()
const playing = ref(false)
let animationFrame = 0
let stopped = false

function compile(gl: WebGLRenderingContext, type: number, source: string) {
  const shader = gl.createShader(type)!
  gl.shaderSource(shader, source)
  gl.compileShader(shader)
  return shader
}

function startAnimation(gl: WebGLRenderingContext, videoElement: HTMLVideoElement) {
  const program = gl.createProgram()!
  gl.attachShader(program, compile(gl, gl.VERTEX_SHADER, VERTEX_SHADER))
  gl.attachShader(program, compile(gl, gl.FRAGMENT_SHADER, FRAGMENT_SHADER))
  gl.linkProgram(program)
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) return
  gl.useProgram(program)

  // One triangle strip covering the canvas.
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer())
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW)
  const position = gl.getAttribLocation(program, 'position')
  gl.enableVertexAttribArray(position)
  gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0)

  gl.bindTexture(gl.TEXTURE_2D, gl.createTexture())
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE)
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE)
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR)
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR)
  const contentHeight = gl.getUniformLocation(program, 'contentHeight')

  const draw = () => {
    if (stopped) return
    if (videoElement.readyState >= videoElement.HAVE_CURRENT_DATA && videoElement.videoHeight) {
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, videoElement)
      gl.uniform1f(contentHeight, HEIGHT / videoElement.videoHeight)
      gl.clear(gl.COLOR_BUFFER_BIT)
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4)
      playing.value = true
    }
    animationFrame = requestAnimationFrame(draw)
  }
  videoElement.play().then(draw, () => {})
}

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  const gl = canvas.value?.getContext('webgl', { premultipliedAlpha: true, alpha: true })
  if (!gl || !video.value) return
  gl.clearColor(0, 0, 0, 0)
  startAnimation(gl, video.value)
})

onBeforeUnmount(() => {
  stopped = true
  cancelAnimationFrame(animationFrame)
  video.value?.pause()
})
</script>

<template>
  <div class="stage">
    <img
      v-show="!playing"
      class="layer"
      :src="withBase('/vtk-logo-3d.png')"
      :width="WIDTH"
      :height="HEIGHT"
      alt="VTK logo in 3D"
    />
    <canvas v-show="playing" ref="canvas" class="layer" :width="WIDTH" :height="HEIGHT" aria-hidden="true" />
    <!-- Source frames only; drawn through the canvas. Kept rendered (not
         display: none) because some browsers stop decoding hidden video. -->
    <video
      ref="video"
      class="source"
      :src="withBase('/vtk-logo-3d.mp4')"
      muted
      loop
      playsinline
      preload="auto"
      aria-hidden="true"
    />
  </div>
</template>

<style scoped>
.stage {
  position: relative;
  width: min(560px, 100%);
  aspect-ratio: 1200 / 644;
  margin-bottom: 16px;
}

.layer {
  display: block;
  width: 100%;
  height: 100%;
}

.source {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}
</style>
