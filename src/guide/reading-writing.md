# Reading & Writing Data

Working with file formats and I/O in VTK.

## VTK Native Formats

- **Legacy format** (.vtk) — Simple, human-readable format
- **XML formats** (.vtp, .vtu, .vti, .vtr, .vts) — Modern, efficient, supports compression
- **VTKHDF** (.vtkhdf) — HDF5-based format for parallel I/O and time series

## Common Scientific Formats

- Exodus II — Finite element data
- CGNS — CFD data
- NetCDF — Multi-dimensional array data
- HDF5 — Hierarchical data
- XDMF — Flexible scientific data format

## Medical Imaging Formats

- DICOM — Medical imaging standard
- NIfTI — Neuroimaging
- NRRD — Nearly Raw Raster Data
- MetaImage — Simple image format

## Geometry Formats

- STL, OBJ, PLY — Polygonal meshes
- glTF — Modern 3D format with materials
- STEP/IGES — CAD formats

## Topics Covered

- Choosing the right file format
- Reading data with VTK readers
- Writing data with VTK writers
- Compression options
- Parallel I/O for large datasets
- Converting between formats
