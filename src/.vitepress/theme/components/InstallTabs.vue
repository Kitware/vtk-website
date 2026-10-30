<script setup lang="ts">
import { ref } from 'vue'

// Like VitePress's `::: code-group`, but each tab also links to its package page.
// Tab content comes from a named slot per tab id, so fenced code blocks keep
// their syntax highlighting and copy button.
interface PackageLink {
  text: string
  href: string
}

interface InstallTab {
  id: string
  label: string
  links: PackageLink[]
}

defineProps<{ tabs: InstallTab[] }>()

const active = ref(0)
</script>

<template>
  <div class="InstallTabs">
    <div class="tabs" role="tablist">
      <button
        v-for="(tab, index) in tabs"
        :key="tab.id"
        type="button"
        role="tab"
        class="tab"
        :class="{ active: active === index }"
        :aria-selected="active === index"
        @click="active = index"
      >
        {{ tab.label }}
      </button>
    </div>
    <div v-for="(tab, index) in tabs" v-show="active === index" :key="tab.id" class="panel" role="tabpanel">
      <slot :name="tab.id" />
      <p class="links">
        <template v-for="(link, linkIndex) in tab.links" :key="link.href">
          <span v-if="linkIndex > 0" class="separator">·</span>
          <a :href="link.href" target="_blank" rel="noreferrer">{{ link.text }}</a>
        </template>
      </p>
    </div>
  </div>
</template>

<style scoped>
.InstallTabs {
  margin-top: 16px;
}

/* Tab bar styles follow VitePress's vp-code-group. */
.tabs {
  display: flex;
  margin: 0 -24px;
  padding: 0 12px;
  background-color: var(--vp-code-tab-bg);
  overflow-x: auto;
  overflow-y: hidden;
  box-shadow: inset 0 -1px var(--vp-code-tab-divider);
}

@media (min-width: 640px) {
  .tabs {
    margin: 0;
    border-radius: 8px 8px 0 0;
  }
}

.tab {
  position: relative;
  padding: 0 12px;
  line-height: 48px;
  font-size: 14px;
  font-weight: 500;
  color: var(--vp-code-tab-text-color);
  white-space: nowrap;
  transition: color 0.25s;
}

.tab::after {
  position: absolute;
  right: 8px;
  bottom: 0;
  left: 8px;
  height: 2px;
  border-radius: 2px;
  content: '';
  background-color: transparent;
  transition: background-color 0.25s;
}

.tab:hover {
  color: var(--vp-code-tab-hover-text-color);
}

.tab.active {
  color: var(--vp-code-tab-active-text-color);
}

.tab.active::after {
  background-color: var(--vp-code-tab-active-bar-color);
}

.panel :deep(div[class*='language-']) {
  margin-top: 0 !important;
  border-top-left-radius: 0 !important;
  border-top-right-radius: 0 !important;
}

.links {
  margin: 8px 0 0;
  font-size: 14px;
  text-align: right;
}

.separator {
  margin: 0 8px;
  color: var(--vp-c-text-3);
}
</style>
