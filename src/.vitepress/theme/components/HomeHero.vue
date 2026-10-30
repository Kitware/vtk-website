<script setup lang="ts">
import { useData } from 'vitepress'
import { VPButton } from 'vitepress/theme'
import HeroAnimation from './HeroAnimation.vue'

const { frontmatter } = useData()
</script>

<template>
  <section v-if="frontmatter.intro" class="HomeHero">
    <HeroAnimation />

    <h1 class="heading">
      <span class="name">{{ frontmatter.intro.name }}</span>
      <span v-if="frontmatter.intro.text" class="text">{{ frontmatter.intro.text }}</span>
    </h1>
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
  display: flex;
  flex-direction: column;
  margin-top: 8px;
}

.name {
  font-size: 56px;
  line-height: 64px;
  font-weight: 700;
  letter-spacing: -0.02em;
  background: var(--vp-home-hero-name-background);
  -webkit-background-clip: text;
  background-clip: text;
  color: var(--vp-home-hero-name-color);
}

.text {
  font-size: 28px;
  line-height: 36px;
  font-weight: 600;
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

  .name {
    font-size: 72px;
    line-height: 80px;
  }

  .text {
    font-size: 36px;
    line-height: 44px;
  }

  .tagline {
    font-size: 20px;
  }
}
</style>
