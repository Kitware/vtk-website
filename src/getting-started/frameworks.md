# Using VTK through Frameworks

You don't need to use VTK directly. Several higher-level frameworks provide easier access to VTK's capabilities.

## ParaView — No-Code Visualization

[ParaView](/ecosystem/paraview) is a full GUI application for data analysis and visualization. No programming required.

- Load data files and apply filters interactively
- Create publication-quality visualizations
- Script with Python for automation
- Scale from laptops to supercomputers

## Trame — Web Applications with Python

[Trame](/ecosystem/trame) lets you build interactive web visualization applications using only Python.

```bash
pip install trame trame-vtk trame-vuetify
```

## PyVista — Pythonic 3D Plotting

[PyVista](/ecosystem/pyvista) wraps VTK with a NumPy-friendly API for quick 3D plotting and mesh analysis.

```bash
pip install pyvista
```

```python
import pyvista as pv
mesh = pv.Sphere()
mesh.plot()
```

## Which Framework?

| Framework | Use Case |
|-----------|----------|
| **ParaView** | Interactive exploration, no coding needed |
| **Trame** | Building web-based visualization apps |
| **PyVista** | Quick 3D plotting in Python scripts and notebooks |
| **Direct VTK** | Maximum control and customization |
