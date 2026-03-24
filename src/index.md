---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "VTK"
  text: "The Visualization Toolkit"
  tagline: "A visualization engine for everyone"
  image:
    src: /hero.png
    alt: VTK Logo
  actions:
    - theme: brand
      text: Getting Started
      link: /getting-started/
    - theme: alt
      text: Download
      link: /download/
    - theme: alt
      text: User's Guide
      link: /guide/

features:
  - title: Data Model
    details: Flexible data structures for structured and unstructured grids, polygonal meshes, images, and volumes. Represent virtually any type of scientific data from medical imaging to engineering simulations.
  - title: Data I/O
    details: Read and write over 50 file formats including DICOM, Exodus, CGNS, glTF, NetCDF, STL, and VTK's own XML and HDF5-based formats. Get your data in and out with ease.
  - title: Extensive Filter Library
    details: A vast collection of processing filters connected through a pipeline architecture. Transform, analyze, contour, clip, threshold, and derive new data from existing datasets.
  - title: Rendering
    details: High-quality 3D surface rendering, GPU-accelerated volume rendering, and photorealistic ray tracing via Intel OSPRay. From interactive exploration to publication-ready images.
  - title: Multi-Language
    details: Native C++ core with full Python wrappings and JavaScript support via vtk.js and WebAssembly. Use VTK in the language and environment that works best for you.
  - title: Open Source & Proven
    details: BSD-licensed and free for any use. Over 30 years of active development, trusted by national laboratories, medical institutions, and industry worldwide.
---
