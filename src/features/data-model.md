# Data Model

VTK's data model provides flexible, powerful data structures for representing virtually any type of scientific data.

## Core Data Structures

- **vtkImageData** — Regular grids for images and volumes (2D and 3D)
- **vtkRectilinearGrid** — Axis-aligned grids with variable spacing
- **vtkStructuredGrid** — Curvilinear grids with explicit point coordinates
- **vtkUnstructuredGrid** — Arbitrary combinations of cell types
- **vtkPolyData** — Polygonal meshes (vertices, lines, polygons, triangle strips)
- **vtkMultiBlockDataSet** — Hierarchical collections of datasets

## Data Arrays

- Support for all common numeric types (int, float, double, etc.)
- Named arrays for scalars, vectors, tensors, and other field data
- Point data and cell data associations
- Global field data for metadata

## Key Design Principles

- **Generality** — Handle structured and unstructured data uniformly
- **Efficiency** — Memory-efficient storage with zero-copy data sharing
- **Extensibility** — Custom data types through subclassing
- **Interoperability** — NumPy integration in Python, zero-copy with other frameworks
