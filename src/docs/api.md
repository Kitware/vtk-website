# API Reference

Links to VTK API documentation for all supported languages.

## C++ API

The C++ API is the primary interface to VTK. Auto-generated documentation is available via Doxygen:

- [VTK Nightly Doxygen](https://vtk.org/doc/nightly/html/) — Latest development API
- Class hierarchy, method signatures, and inheritance diagrams
- Search by class name or namespace

## Python API

VTK Python wrappings mirror the C++ API closely:

- All VTK classes are accessible from Python
- Automatic type conversion for common types
- NumPy integration for data arrays
- Python-specific utilities in `vtkmodules.util`

## CMake API

VTK provides CMake functions for building applications:

- `find_package(VTK)` — Locate VTK installation
- `vtk_module_autoinit()` — Configure module initialization
- Module-based component selection
- Custom module development

## Conventions

- Class names start with `vtk` prefix (e.g., `vtkActor`)
- Set/Get methods for properties (e.g., `SetColor()`, `GetColor()`)
- Boolean methods use On/Off suffix (e.g., `VisibilityOn()`, `VisibilityOff()`)
- Factory methods via `New()` (C++) or class constructor (Python)
