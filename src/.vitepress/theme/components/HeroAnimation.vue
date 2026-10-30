<script setup lang="ts">
// Placeholder for the 3D VTK logo + supported-languages animation.
// Swap the contents of `.stage` for the real animation; the stage
// reserves a fixed square so the layout won't shift when it loads.
</script>

<template>
  <div class="stage" role="img" aria-label="VTK logo">
    <img class="logo" src="/hero.png" alt="" />
  </div>
</template>

<style scoped>
.stage {
  position: relative;
  width: min(420px, 80vw);
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stage::before {
  content: '';
  position: absolute;
  inset: 12%;
  border-radius: 50%;
  background-image: var(--vp-home-hero-image-background-image);
  filter: var(--vp-home-hero-image-filter);
  opacity: 0.6;
}

.logo {
  position: relative;
  width: 80%;
  height: auto;
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

@media (prefers-reduced-motion: reduce) {
  .logo { animation: none; }
}
</style>
