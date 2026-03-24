# Supported Data Formats

VTK supports reading and writing over 50 file formats. This page catalogs the supported formats organized by category.

## VTK Native Formats

| Format | Extension | Read | Write | Description |
|--------|-----------|------|-------|-------------|
| VTK Legacy | .vtk | Yes | Yes | Simple ASCII/binary format |
| VTK XML | .vtp, .vtu, .vti, .vtr, .vts | Yes | Yes | Modern format with compression |
| VTKHDF | .vtkhdf | Yes | Yes | HDF5-based, parallel I/O |

## Scientific Data

| Format | Extension | Read | Write | Description |
|--------|-----------|------|-------|-------------|
| Exodus II | .e, .exo | Yes | Yes | Finite element (Sandia) |
| CGNS | .cgns | Yes | Yes | CFD data |
| NetCDF | .nc | Yes | No | Array-oriented data |
| HDF5 | .h5 | Yes | No | Hierarchical data |
| XDMF | .xdmf | Yes | Yes | Flexible XML+HDF5 |

## Medical Imaging

| Format | Extension | Read | Write | Description |
|--------|-----------|------|-------|-------------|
| DICOM | .dcm | Yes | No | Medical imaging standard |
| NIfTI | .nii, .nii.gz | Yes | Yes | Neuroimaging |
| NRRD | .nrrd | Yes | Yes | Nearly Raw Raster Data |
| MetaImage | .mha, .mhd | Yes | Yes | Simple image format |

## Geometry

| Format | Extension | Read | Write | Description |
|--------|-----------|------|-------|-------------|
| STL | .stl | Yes | Yes | Stereolithography |
| OBJ | .obj | Yes | Yes | Wavefront |
| PLY | .ply | Yes | Yes | Polygon file format |
| glTF | .gltf, .glb | Yes | Yes | GL Transmission Format |

*This is a subset of supported formats. See the full list in the VTK documentation.*
