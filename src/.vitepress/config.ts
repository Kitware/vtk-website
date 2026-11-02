import { defineConfig } from 'vitepress'

// Path the site is served under: '/vtk-website/' on GitHub Pages, '/' on a custom
// domain or a Firebase preview. CI sets VITEPRESS_BASE; it defaults to '/'.
const base = process.env.VITEPRESS_BASE || '/'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base,
  title: "VTK",
  description: "The Visualization Toolkit (VTK) is open source software for manipulating and displaying scientific data. It comes with state-of-the-art tools for 3D rendering.",
  head: [['link', { rel: 'icon', href: `${base}favicon.ico` }]],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      {
        text: 'About',
        items: [
          { text: 'Overview', link: '/about/' },
          { text: 'Features', link: '/features/' },
          { text: 'Solutions', link: '/solutions/' },
          { text: 'History', link: '/about/history' },
          { text: 'License', link: '/about/license' },
          { text: 'Citing VTK', link: '/about/citing' },
          { text: 'Contributors', link: '/about/contributors' }
        ]
      },
      {
        text: 'Ecosystem',
        items: [
          { text: 'Overview', link: '/ecosystem/' },
          { text: 'ParaView', link: '/ecosystem/paraview' },
          { text: 'Trame', link: '/ecosystem/trame' },
          { text: 'PyVista', link: '/ecosystem/pyvista' },
          { text: 'vtk.js', link: '/ecosystem/vtk-js' },
          { text: '3D Slicer', link: '/ecosystem/slicer' }
        ]
      },
      {
        text: 'Learn',
        items: [
          { text: 'Getting Started', link: '/getting-started/' },
          { text: "User's Guide", link: '/guide/' },
          { text: 'Examples', link: '/examples/' },
          { text: 'API Reference', link: '/docs/api' },
          { text: 'Data Formats', link: '/docs/formats' },
          { text: 'Modules', link: '/docs/modules' },
          { text: 'Building from Source', link: '/docs/building' },
          { text: 'VTK Textbook', link: '/docs/textbook' }
        ]
      },
      {
        text: 'Community',
        items: [
          { text: 'Overview', link: '/community/' },
          { text: 'Contributing', link: '/community/contributing' },
          { text: 'Professional Services', link: '/community/services' },
          { text: 'Events', link: '/community/events' },
          { text: 'Gallery', link: '/gallery/' }
        ]
      },
      { text: 'Download', link: '/download/' }
    ],

    sidebar: {
      '/about/': [
        {
          text: 'About VTK',
          items: [
            { text: 'Overview', link: '/about/' },
            { text: 'History', link: '/about/history' },
            { text: 'License', link: '/about/license' },
            { text: 'Citing VTK', link: '/about/citing' },
            { text: 'Logo', link: '/about/logo' },
            { text: 'Contributors', link: '/about/contributors' }
          ]
        }
      ],
      '/features/': [
        {
          text: 'Features',
          items: [
            { text: 'Overview', link: '/features/' },
            { text: 'Data Model', link: '/features/data-model' },
            { text: 'Filters', link: '/features/filters' },
            { text: 'Rendering', link: '/features/rendering' },
            { text: 'Interaction', link: '/features/interaction' },
            { text: 'Charts', link: '/features/charts' },
            { text: 'Parallel Processing', link: '/features/parallel' },
            { text: 'I/O Formats', link: '/features/io' }
          ]
        }
      ],
      '/solutions/': [
        {
          text: 'Solutions',
          items: [
            { text: 'Overview', link: '/solutions/' },
            { text: 'Medical Imaging', link: '/solutions/medical' },
            { text: 'Engineering', link: '/solutions/engineering' },
            { text: 'Geospatial', link: '/solutions/geospatial' },
            { text: 'Scientific', link: '/solutions/scientific' },
            { text: 'Web Visualization', link: '/solutions/web' }
          ]
        }
      ],
      '/ecosystem/': [
        {
          text: 'Ecosystem',
          items: [
            { text: 'Overview', link: '/ecosystem/' },
            { text: 'ParaView', link: '/ecosystem/paraview' },
            { text: 'Trame', link: '/ecosystem/trame' },
            { text: 'PyVista', link: '/ecosystem/pyvista' },
            { text: 'vtk.js', link: '/ecosystem/vtk-js' },
            { text: '3D Slicer', link: '/ecosystem/slicer' }
          ]
        }
      ],
      '/getting-started/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Overview', link: '/getting-started/' },
            { text: 'Python', link: '/getting-started/python' },
            { text: 'C++', link: '/getting-started/cpp' },
            { text: 'JavaScript', link: '/getting-started/javascript' },
            { text: 'Frameworks', link: '/getting-started/frameworks' }
          ]
        }
      ],
      '/guide/': [
        {
          text: "User's Guide",
          items: [
            { text: 'Overview', link: '/guide/' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'System Overview', link: '/guide/system-overview' },
            { text: 'The Basics', link: '/guide/basics' },
            { text: 'Visualization Techniques', link: '/guide/visualization' },
            { text: 'Image Processing', link: '/guide/image-processing' },
            { text: 'Volume Rendering', link: '/guide/volume-rendering' },
            { text: 'Information Visualization', link: '/guide/info-vis' },
            { text: 'Geospatial Visualization', link: '/guide/geospatial' },
            { text: 'Building Models', link: '/guide/building-models' },
            { text: 'Time-Varying Data', link: '/guide/time-varying' },
            { text: 'Reading & Writing Data', link: '/guide/reading-writing' },
            { text: 'Interaction & Widgets', link: '/guide/interaction' }
          ]
        }
      ],
      '/docs/': [
        {
          text: 'Documentation',
          items: [
            { text: 'Documentation Hub', link: '/docs/' },
            { text: 'API Reference', link: '/docs/api' },
            { text: 'Data Formats', link: '/docs/formats' },
            { text: 'Modules', link: '/docs/modules' },
            { text: 'Building from Source', link: '/docs/building' },
            { text: 'VTK Textbook', link: '/docs/textbook' }
          ]
        }
      ],
      '/community/': [
        {
          text: 'Community',
          items: [
            { text: 'Overview', link: '/community/' },
            { text: 'Contributing', link: '/community/contributing' },
            { text: 'Professional Services', link: '/community/services' },
            { text: 'Events', link: '/community/events' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'discourse', link: 'https://discourse.vtk.org' },
      { icon: 'gitlab', link: 'https://gitlab.kitware.com/Kitware/vtk' },
      { icon: 'github', link: 'https://github.com/Kitware/vtk' }
    ]
  }
})
