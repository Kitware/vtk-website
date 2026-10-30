<script setup lang="ts">
import { useData, withBase } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <section v-if="frontmatter.highlights" class="HomeHighlights">
    <component
      :is="item.link ? 'a' : 'article'"
      v-for="item in frontmatter.highlights"
      :key="item.title"
      class="card"
      :href="item.link ? withBase(item.link) : undefined"
    >
      <h2 class="title">{{ item.title }}</h2>
      <div class="media">
        <img :src="withBase(item.image)" :alt="item.alt ?? ''" loading="lazy" />
      </div>
      <p class="details">{{ item.details }}</p>
    </component>
  </section>
</template>

<style scoped>
/* 6-column grid: first two cards span half the row, the rest a third. */
.HomeHighlights {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
  max-width: 1152px;
  margin: 0 auto;
  padding: 0 24px;
}

@media (min-width: 640px) {
  .HomeHighlights {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 960px) {
  .HomeHighlights {
    grid-template-columns: repeat(6, 1fr);
    padding: 0 64px;
  }

  .card {
    grid-column: span 2;
  }

  .card:nth-child(-n + 2) {
    grid-column: span 3;
  }
}

.card {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--vp-c-bg-soft);
  border-radius: 12px;
  background-color: var(--vp-c-bg-soft);
  padding: 24px;
  color: inherit;
  text-decoration: none;
  transition: border-color 0.25s;
}

a.card:hover {
  border-color: var(--vp-c-brand-1);
}

.title {
  font-size: 18px;
  line-height: 24px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

.media {
  margin: 16px -24px;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background-color: var(--vp-c-bg-alt);
}

.media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

a.card:hover .media img {
  transform: scale(1.04);
}

.details {
  font-size: 14px;
  line-height: 22px;
  color: var(--vp-c-text-2);
}
</style>
