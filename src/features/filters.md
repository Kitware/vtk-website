# Filters

VTK includes over 200 processing filters organized in a pipeline architecture for transforming, analyzing, and deriving new data from existing datasets.

## Pipeline Architecture

VTK uses a demand-driven pipeline where filters are connected to form a dataflow network. Data flows from sources through filters to mappers and actors for rendering.

## Filter Categories

- **Geometric filters** — Contouring (marching cubes), slicing, clipping, cutting
- **Topological filters** — Triangulation, decimation, subdivision, connectivity
- **Attribute filters** — Gradient computation, interpolation, field calculator
- **Statistical filters** — Histogram, descriptive statistics, principal component analysis
- **Temporal filters** — Time interpolation, pathlines, particle tracing
- **Sampling filters** — Probing, resampling, point cloud processing

## Key Features

- **Lazy evaluation** — Filters only execute when output is requested
- **Incremental updates** — Only recompute what has changed
- **Multi-block support** — Process composite datasets transparently
- **Streaming** — Process data in pieces to handle large datasets
- **Composability** — Chain filters freely to build custom workflows
