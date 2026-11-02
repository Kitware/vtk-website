# Installation

How to install VTK on your system.

## Python (Recommended)

The easiest way to install VTK is via pip:

```bash
pip install vtk
```

Pre-built wheels are available for Linux, macOS, and Windows on Python 3.9+.

## C++ — Pre-built Packages

VTK is available through system package managers on many platforms:

- **Ubuntu/Debian**: `apt install libvtk9-dev`
- **macOS (Homebrew)**: `brew install vtk`
- **Windows (vcpkg)**: `vcpkg install vtk`

## C++ — Building from Source

For full control over VTK's configuration, build from source with CMake. See [Building from Source](/docs/building) for detailed instructions.

## Verifying Installation

### Python

```python
import vtk
print(vtk.vtkVersion.GetVTKVersion())
```

### C++

Create a simple CMake project that links against VTK and prints the version number.

## Topics Covered

- System requirements and prerequisites
- Platform-specific installation notes
- Configuring optional dependencies (MPI, OSPRay, etc.)
- Troubleshooting common installation issues
