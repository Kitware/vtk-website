# Getting Started with Python

The fastest way to start using VTK is through Python with pip.

## Installation

```bash
pip install vtk
```

## Your First Visualization

```python
import vtkmodules.all as vtk

# Create a sphere source
sphere = vtk.vtkSphereSource()
sphere.SetRadius(1.0)
sphere.SetThetaResolution(32)
sphere.SetPhiResolution(32)

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer and render window
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(800, 600)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the visualization
render_window.Render()
interactor.Start()
```

## Next Steps

- Explore the [User's Guide](/guide/) for in-depth tutorials
- Browse [examples](https://examples.vtk.org) for more Python code
- Consider [PyVista](/ecosystem/pyvista) for a more Pythonic API
- Try [Trame](/ecosystem/trame) for building web applications
