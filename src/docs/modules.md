# VTK Modules

VTK is organized into a modular architecture. Each module provides a specific set of functionality and declares its dependencies.

## Module System

VTK's module system allows you to:

- Build only the modules you need
- Manage dependencies automatically
- Create custom modules that integrate with VTK
- Reduce binary size by excluding unused functionality

## Core Module Groups

- **Common** — Fundamental data types, math, and system utilities
- **Filters** — Data processing algorithms
- **IO** — File format readers and writers
- **Imaging** — Image processing filters
- **Interaction** — Widgets and interaction styles
- **Rendering** — Rendering infrastructure and backends
- **Views** — High-level visualization views
- **Charts** — 2D charting framework

## Finding Modules

Each VTK class belongs to a specific module. To find which module a class belongs to:

- Check the class documentation
- Use `vtk_module_find_package()` in CMake
- Browse the module listing in the VTK source tree

## Custom Modules

Developers can create custom VTK modules that:

- Extend VTK with new algorithms
- Integrate third-party libraries
- Are discovered and built by VTK's build system
