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
      link: /guide/getting-started

features:
  - title: Data Model
    details: Represent almost any real-world problem related to physical science. The fundamental data structures are particularly well-suited to medical imaging and engineering work that involves finite difference and finite element solutions.
  - title: Filters
    details: Filters inspect input data to produce derived data. A connected set of filters forms a dataflow network. A configurable network turns raw data into more visually comprehensible formats.
  - title: Graphics
    details: Provides abstraction layer over the underlying graphics library (OpenGL for the most part). This higher level simplifies the task of creating compelling visualizations.
  - title: Data Interaction
    details: Helps you understand the content, shape and meaning of your data. 3D widgets, interactors and interfaces to other libraries (like trame and Qt) make it easy to present your visualizations and allow users to explore them.
  - title: 2D Plots and Charts
    details: Create journal-quality scientific charts, plots, and graphs with the 2D charting classes. Supports a variety of plot types including line, scatter, bar, box, and pie charts.
  - title: Parallel Processing
    details: Both shared memory (using multi-threading) and distributed memory (using MPI) approaches are supported. This allows VTK to handle large datasets and perform complex computations efficiently.
---

