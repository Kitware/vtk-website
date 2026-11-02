---
outline: [2, 3]
---

<script setup>
import data from './releases.json'

const [latest, ...previous] = data.releases

const installTabs = [
  { id: 'pip', label: 'pip', links: [{ text: 'vtk on PyPI', href: 'https://pypi.org/project/vtk/' }] },
  { id: 'conda', label: 'conda', links: [{ text: 'vtk on conda-forge', href: 'https://anaconda.org/conda-forge/vtk' }] },
  {
    id: 'debian',
    label: 'Ubuntu / Debian',
    links: [
      { text: 'vtk9 on Ubuntu', href: 'https://launchpad.net/ubuntu/+source/vtk9' },
      { text: 'vtk9 on Debian', href: 'https://tracker.debian.org/pkg/vtk9' },
    ],
  },
  { id: 'fedora', label: 'Fedora', links: [{ text: 'vtk on Fedora', href: 'https://packages.fedoraproject.org/pkgs/vtk/' }] },
  { id: 'homebrew', label: 'macOS (Homebrew)', links: [{ text: 'vtk on Homebrew', href: 'https://formulae.brew.sh/formula/vtk' }] },
  { id: 'vcpkg', label: 'Windows (vcpkg)', links: [{ text: 'vtk on vcpkg', href: 'https://vcpkg.io/en/package/vtk' }] },
]
</script>

# Download VTK

<p class="download-banner">
  Latest release: <strong>VTK {{ latest.version }}</strong> ·
  <a :href="`https://docs.vtk.org/en/latest/release_details/${latest.version.split('.').slice(0, 2).join('.')}.html`">Release notes</a> ·
  <a href="#previous-releases">Previous releases</a>
</p>

## Install

Pick your package manager. Each one installs the latest release it packages.

<InstallTabs :tabs="installTabs">
<template #pip>

```sh
pip install vtk
```

</template>
<template #conda>

```sh
conda install -c conda-forge vtk
```

</template>
<template #debian>

```sh
# C++ headers and libraries
sudo apt install libvtk9-dev
# Python bindings
sudo apt install python3-vtk9
```

</template>
<template #fedora>

```sh
# C++ headers and libraries
sudo dnf install vtk-devel
# Python bindings
sudo dnf install python3-vtk
```

</template>
<template #homebrew>

```sh
brew install vtk
```

</template>
<template #vcpkg>

```sh
vcpkg install vtk
```

</template>
</InstallTabs>

Python wheels on PyPI support CPython {{ data.python.versions }} on {{ data.python.platforms }}.

::: tip Distribution packages can lag behind
Linux distributions, Homebrew, and vcpkg update on their own schedules, so they may ship an older VTK than {{ latest.version }}. Use pip or conda for the newest release, or [build from source](/docs/building).
:::

## Development Builds

Wheels built from the development branch are published to VTK's package registry. Their versions look like `9.7.20261026.dev0`.

```sh
pip install --pre --extra-index-url https://wheels.vtk.org vtk
```

::: warning
Development builds are untested between releases and may change without notice. Don't use them in production.
:::

## Source Code

### Latest Release

<ReleaseFiles :release="latest" />

You only need the source archive to build VTK. The data archives are for running VTK's test suite.

### Git Repository

```sh
git clone https://gitlab.kitware.com/vtk/vtk.git
```

See [Building from Source](/docs/building) for compilation instructions.

## Previous Releases

<details v-for="release in previous" :key="release.version" class="details custom-block">
  <summary>VTK {{ release.version }}</summary>
  <ReleaseFiles :release="release" />
</details>

Older releases are in the [release archive](https://vtk.org/files/release/).

---

<p class="download-legal">
  This software may not be exported in violation of any U.S. export laws or regulations. For more information on export control, see <a href="https://www.kitware.com/legal/">Kitware Legal</a>.
</p>

<style>
.download-banner {
  font-size: 16px;
  color: var(--vp-c-text-2);
}

.download-legal {
  font-size: 13px;
  color: var(--vp-c-text-3);
}
</style>
