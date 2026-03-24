# Building VTK from Source

Instructions for compiling VTK from source with CMake.

## Prerequisites

- **CMake** 3.12 or later
- **C++ compiler** with C++17 support (GCC 8+, Clang 7+, MSVC 2019+)
- **Git** for cloning the repository
- **OpenGL** development libraries

## Quick Build

```bash
git clone https://gitlab.kitware.com/vtk/vtk.git
cd vtk
mkdir build && cd build
cmake ..
cmake --build . -j$(nproc)
```

## Common CMake Options

| Option | Default | Description |
|--------|---------|-------------|
| `VTK_WRAP_PYTHON` | OFF | Build Python bindings |
| `VTK_WRAP_JAVA` | OFF | Build Java bindings |
| `VTK_USE_MPI` | OFF | Enable MPI parallel support |
| `VTK_MODULE_ENABLE_*` | DEFAULT | Enable/disable specific modules |
| `VTK_ENABLE_OSPRAY` | OFF | Intel OSPRay ray tracing |

## Platform Notes

### Linux
- Install OpenGL dev packages: `apt install libgl1-mesa-dev`
- Optional: X11 or Wayland development packages

### macOS
- Xcode command line tools required
- OpenGL provided by the system

### Windows
- Visual Studio 2019+ with C++ workload
- Ninja generator recommended for faster builds

## Topics Covered

- Detailed CMake configuration options
- Module selection and dependency management
- Building with optional features (MPI, OSPRay, Qt)
- Installing VTK system-wide
- Troubleshooting build issues
