---
layout: home
markdownStyles: false

intro:
  text: "The Visualization Toolkit"
  tagline: "A visualization engine for everyone"
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

highlights:
  - title: Data Model
    image: /images/home/data-model.png
    alt: Liquid oxygen post flow field on a structured grid
    link: /features/data-model
    details: Flexible data structures for structured and unstructured grids, polygonal meshes, images, and volumes. Represent virtually any type of scientific data from medical imaging to engineering simulations.
  - title: Rendering
    image: /images/home/rendering.png
    alt: Segmented frog anatomy rendered as translucent surfaces
    link: /features/rendering
    details: High-quality 3D surface rendering, GPU-accelerated volume rendering, and photorealistic ray tracing via Intel OSPRay. From interactive exploration to publication-ready images.
  - title: Extensive Filter Library
    image: /images/home/filters.png
    alt: Streamlines of air flow through a kitchen
    link: /features/filters
    details: A vast collection of processing filters connected through a pipeline architecture. Transform, analyze, contour, clip, threshold, and derive new data from existing datasets.
  - title: Data I/O
    image: /images/home/data-io.png
    alt: Elevation map of Honolulu, Hawaii
    link: /features/io
    details: Read and write over 50 file formats including DICOM, Exodus, CGNS, glTF, NetCDF, STL, and VTK's own XML and HDF5-based formats. Get your data in and out with ease.
  - title: Multi-Language
    image: /images/home/multi-language.png
    alt: Blood flow velocity glyphs in a carotid artery
    link: /getting-started/#by-language
    details: Native C++ core with full Python wrappings and JavaScript support via vtk.js and WebAssembly. Use VTK in the language and environment that works best for you.

closing:
  title: Open Source & Proven
  details: BSD-licensed and free for any use. Over 30 years of active development, trusted by national laboratories, medical institutions, and industry worldwide.
  actions:
    - theme: alt
      text: License
      link: /about/license
    - theme: alt
      text: Citing VTK
      link: /about/citing
---

<HomeHero />
<HomeHighlights />
<HomeClosing />
