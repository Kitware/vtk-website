# Getting Started with C++

Build VTK applications in C++ for maximum performance.

## Prerequisites

- A C++17-compatible compiler (GCC, Clang, or MSVC)
- [CMake](https://cmake.org/) 3.12 or later
- VTK installed or built from source (see [Building from Source](/docs/building))

## CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.12)
project(MyVTKApp)

find_package(VTK REQUIRED COMPONENTS
  CommonCore
  FiltersSources
  InteractionStyle
  RenderingCore
  RenderingOpenGL2
)

add_executable(MyVTKApp main.cpp)
target_link_libraries(MyVTKApp PRIVATE ${VTK_LIBRARIES})
vtk_module_autoinit(TARGETS MyVTKApp MODULES ${VTK_LIBRARIES})
```

## Your First Program (main.cpp)

```cpp
#include <vtkActor.h>
#include <vtkPolyDataMapper.h>
#include <vtkRenderer.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkSphereSource.h>
#include <vtkNew.h>

int main() {
    vtkNew<vtkSphereSource> sphere;
    sphere->SetRadius(1.0);
    sphere->SetThetaResolution(32);
    sphere->SetPhiResolution(32);

    vtkNew<vtkPolyDataMapper> mapper;
    mapper->SetInputConnection(sphere->GetOutputPort());

    vtkNew<vtkActor> actor;
    actor->SetMapper(mapper);

    vtkNew<vtkRenderer> renderer;
    renderer->AddActor(actor);
    renderer->SetBackground(0.1, 0.2, 0.4);

    vtkNew<vtkRenderWindow> window;
    window->AddRenderer(renderer);
    window->SetSize(800, 600);

    vtkNew<vtkRenderWindowInteractor> interactor;
    interactor->SetRenderWindow(window);

    window->Render();
    interactor->Start();

    return 0;
}
```

## Build and Run

```bash
mkdir build && cd build
cmake ..
cmake --build .
./MyVTKApp
```

## Next Steps

- See [Building from Source](/docs/building) for compiling VTK itself
- Browse [C++ examples](https://examples.vtk.org) for more code
- Read the [User's Guide](/guide/) for in-depth tutorials
