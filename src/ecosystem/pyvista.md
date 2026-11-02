# PyVista

[PyVista](https://docs.pyvista.org/) is a Pythonic interface to VTK that streamlines 3D plotting and mesh analysis.

## Overview

PyVista wraps VTK with a NumPy-friendly API, making it easy to create visualizations with just a few lines of Python. It is particularly popular in the scientific Python community for its intuitive interface.

## Key Features

- **Pythonic API** — NumPy-style access to VTK data structures
- **Easy plotting** — Create 3D visualizations in a few lines of code
- **Mesh analysis** — Boolean operations, smoothing, decimation, and more
- **Jupyter support** — Interactive 3D widgets in notebooks
- **File I/O** — Read and write many mesh formats
- **Integration** — Works with NumPy, SciPy, and other scientific Python libraries

## Getting Started

```bash
pip install pyvista
```

```python
import pyvista as pv
mesh = pv.Sphere()
mesh.plot()
```

## Links

- [PyVista documentation](https://docs.pyvista.org/)
- [PyVista on GitHub](https://github.com/pyvista/pyvista)
- [PyVista examples](https://docs.pyvista.org/examples/)
