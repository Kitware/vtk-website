<script setup lang="ts">
import { useData } from 'vitepress'
import { VPButton } from 'vitepress/theme'
import HeroAnimation from './HeroAnimation.vue'

const { frontmatter } = useData()
</script>

<template>
  <section v-if="frontmatter.intro" class="HomeHero">
    <HeroAnimation />

    <h1 class="heading">{{ frontmatter.intro.text }}</h1>
    <p v-if="frontmatter.intro.tagline" class="tagline">{{ frontmatter.intro.tagline }}</p>

    <div v-if="frontmatter.intro.actions" class="actions">
      <VPButton
        v-for="action in frontmatter.intro.actions"
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
.HomeHero {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 32px 24px 64px;
}

.heading {
  font-size: 36px;
  line-height: 44px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--vp-c-text-1);
}

.tagline {
  margin-top: 12px;
  font-size: 18px;
  line-height: 28px;
  color: var(--vp-c-text-2);
}

.actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 32px;
}

@media (min-width: 768px) {
  .HomeHero {
    padding-top: 48px;
    padding-bottom: 96px;
  }

  .heading {
    font-size: 56px;
    line-height: 64px;
  }

  .tagline {
    font-size: 20px;
  }
}
</style>
