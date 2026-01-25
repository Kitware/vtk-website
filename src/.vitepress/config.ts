import { defineConfig } from 'vitepress'
// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: '/vtk-website/',
  title: "VTK",
  description: "The Visualization Toolkit (VTK) is open source software for manipulating and displaying scientific data. It comes with state-of-the-art tools for 3D rendering.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'home', link: '/' },
      { text: 'guide', link: '/guide/' }
    ],

    sidebar: [
      {
        text: 'guide',
        items: [
          // TODO: add guide pages here
        ]
      }
    ],

    socialLinks: [
      { icon: 'discourse', link: 'https://discourse.vtk.org' },
      { icon: 'gitlab', link: 'https://gitlab.kitware.com/Kitware/vtk' },
      { icon: 'github', link: 'https://github.com/Kitware/vtk' }
    ]
  }
})
