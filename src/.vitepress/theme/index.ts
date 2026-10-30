import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import HomeHero from './components/HomeHero.vue'
import HomeHighlights from './components/HomeHighlights.vue'
import HomeClosing from './components/HomeClosing.vue'
import InstallTabs from './components/InstallTabs.vue'
import ReleaseFiles from './components/ReleaseFiles.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('HomeHero', HomeHero)
    app.component('HomeHighlights', HomeHighlights)
    app.component('HomeClosing', HomeClosing)
    app.component('InstallTabs', InstallTabs)
    app.component('ReleaseFiles', ReleaseFiles)
  },
} satisfies Theme
