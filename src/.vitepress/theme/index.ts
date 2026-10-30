import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import HomeHero from './components/HomeHero.vue'
import HomeHighlights from './components/HomeHighlights.vue'
import HomeClosing from './components/HomeClosing.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('HomeHero', HomeHero)
    app.component('HomeHighlights', HomeHighlights)
    app.component('HomeClosing', HomeClosing)
  },
} satisfies Theme
