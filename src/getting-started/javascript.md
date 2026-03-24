# Getting Started with JavaScript

Bring VTK visualization to the web browser.

## vtk.js

vtk.js is a JavaScript implementation of VTK for client-side rendering in the browser.

### Installation

```bash
npm install @kitware/vtk.js
```

### Quick Example

```javascript
import '@kitware/vtk.js/Rendering/Profiles/Geometry';
import vtkFullScreenRenderWindow from '@kitware/vtk.js/Rendering/Misc/FullScreenRenderWindow';
import vtkSphereSource from '@kitware/vtk.js/Filters/Sources/SphereSource';
import vtkMapper from '@kitware/vtk.js/Rendering/Core/Mapper';
import vtkActor from '@kitware/vtk.js/Rendering/Core/Actor';

const fullScreenRenderer = vtkFullScreenRenderWindow.newInstance();
const renderer = fullScreenRenderer.getRenderer();

const sphere = vtkSphereSource.newInstance();
const mapper = vtkMapper.newInstance();
mapper.setInputConnection(sphere.getOutputPort());

const actor = vtkActor.newInstance();
actor.setMapper(mapper);

renderer.addActor(actor);
renderer.resetCamera();
fullScreenRenderer.getRenderWindow().render();
```

## WebAssembly (WASM)

VTK can also be compiled to WebAssembly for near-native performance in the browser. This approach provides access to the full C++ VTK API.

## Next Steps

- [vtk.js documentation](https://kitware.github.io/vtk-js/)
- [vtk.js examples](https://kitware.github.io/vtk-js/examples/)
- [Trame](/ecosystem/trame) for Python-based web applications
