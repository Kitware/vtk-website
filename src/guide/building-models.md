# Building Models

Constructing geometric models programmatically in VTK.

## Procedural Sources

- Basic shapes: sphere, cube, cylinder, cone, disk, plane
- Parametric surfaces: superquadric, ellipsoid, torus
- Text: 3D text extrusion, vector text
- Arrow and axis sources for annotations

## Constructive Solid Geometry (CSG)

- Boolean operations (union, intersection, difference)
- vtkBooleanOperationPolyDataFilter
- Combining primitive shapes into complex models

## Mesh Construction

- Building meshes from points and connectivity
- Delaunay triangulation (2D and 3D)
- Surface reconstruction from point clouds
- Implicit function-based modeling

## Mesh Processing

- Smoothing (Laplacian, windowed sinc)
- Decimation (polygon reduction)
- Subdivision (Loop, Butterfly)
- Normal generation
- Cleaning and validation

## Topics Covered

- Creating custom geometric models
- Extrusion and revolution of 2D profiles
- Clipping and cutting operations
- Mesh quality assessment and improvement
- Exporting models for 3D printing
