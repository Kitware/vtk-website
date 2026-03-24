# Web Visualization

VTK-based visualization can be delivered through web browsers using several complementary technologies.

## Technologies

### vtk.js
A JavaScript library that implements a subset of VTK's functionality natively in the browser using WebGL. Ideal for client-side visualization without a server.

- [vtk.js on GitHub](https://github.com/Kitware/vtk-js)

### Trame
A Python framework for building interactive web applications with VTK. Trame runs VTK on the server and streams results to the browser, or uses vtk.js for client-side rendering.

- [Trame documentation](https://trame.readthedocs.io/)

### WebAssembly (WASM)
VTK can be compiled to WebAssembly, bringing the full C++ VTK library to the browser with near-native performance.

## Choosing an Approach

| Approach | Best For |
|----------|----------|
| **vtk.js** | Client-side rendering, lightweight visualizations |
| **Trame (server)** | Large datasets, full VTK feature set, Python workflows |
| **Trame (client)** | Hybrid approach, progressive enhancement |
| **WASM** | Full C++ VTK in browser, offline-capable applications |

## Related Projects

- [vtk.js](/ecosystem/vtk-js)
- [Trame](/ecosystem/trame)
