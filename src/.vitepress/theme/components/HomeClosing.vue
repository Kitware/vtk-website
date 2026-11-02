<script setup lang="ts">
import { useData } from 'vitepress'
import { VPButton } from 'vitepress/theme'

const { frontmatter } = useData()
</script>

<template>
  <section v-if="frontmatter.closing" class="HomeClosing">
    <h2 class="title">{{ frontmatter.closing.title }}</h2>
    <p class="details">{{ frontmatter.closing.details }}</p>
    <div v-if="frontmatter.closing.actions" class="actions">
      <VPButton
        v-for="action in frontmatter.closing.actions"
        :key="action.link"
        tag="a"
        size="medium"
        :theme="action.theme"
        :text="action.text"
        :href="action.link"
      />
    </div>
  </section>
</template>

<style scoped>
.HomeClosing {
  max-width: 720px;
  margin: 96px auto 0;
  padding: 48px 24px 0;
  border-top: 1px solid var(--vp-c-divider);
  text-align: center;
}

.title {
  font-size: 28px;
  line-height: 36px;
  font-weight: 700;
  color: var(--vp-c-text-1);
}

.details {
  margin-top: 16px;
  font-size: 17px;
  line-height: 28px;
  color: var(--vp-c-text-2);
}

.actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 24px;
}
</style>
