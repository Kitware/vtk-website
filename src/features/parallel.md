# Parallel Processing

VTK supports both shared-memory and distributed-memory parallelism for handling large-scale datasets and computations.

## Multi-Threading

- **vtkSMPTools** — Thread-level parallelism with configurable backends
- Support for TBB, OpenMP, and STDThread backends
- Automatic parallelization of many built-in filters
- Thread-safe data structures for concurrent access

## Distributed Computing (MPI)

- **vtkMPIController** — MPI-based distributed processing
- Distributed data handling with ghost cells
- Parallel I/O for large datasets
- Sort-last parallel rendering with compositing

## Key Capabilities

- Process datasets too large for a single machine
- Scale from laptops to supercomputers
- Automatic data partitioning and load balancing
- Compatible with HPC job schedulers (Slurm, PBS, etc.)

## Use Cases

- Large-scale simulation post-processing
- In-situ visualization during simulation runs
- Batch processing of many datasets
- Interactive exploration of distributed data
