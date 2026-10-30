<script setup lang="ts">
import { computed, ref } from 'vue'

interface ReleaseFile {
  kind: string
  name: string
  size: string
  sha256?: string
  md5?: string
}

interface Release {
  version: string
  date: string
  files: ReleaseFile[]
}

const props = defineProps<{ release: Release }>()

const DESCRIPTIONS: Record<string, string> = {
  source: 'Source code',
  data: 'Test data, as an ExternalData object store',
  'data-files': 'Test data, laid out at its source-tree paths',
  'large-data': 'Large test data, as an ExternalData object store',
  'large-data-files': 'Large test data, laid out at its source-tree paths',
  docs: 'Offline HTML documentation',
}

// Releases live under /files/release/<major>.<minor>/
const series = computed(() => props.release.version.split('.').slice(0, 2).join('.'))
const baseUrl = computed(() => `https://vtk.org/files/release/${series.value}/`)

const date = computed(() =>
  new Date(`${props.release.date}T00:00:00Z`).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    timeZone: 'UTC',
  }),
)

const checksumLabel = computed(() => (props.release.files.some((file) => file.sha256) ? 'SHA-256' : 'MD5'))

const copiedName = ref<string>()

async function copyChecksum(file: ReleaseFile) {
  await navigator.clipboard.writeText(file.sha256 ?? file.md5 ?? '')
  copiedName.value = file.name
  setTimeout(() => {
    if (copiedName.value === file.name) copiedName.value = undefined
  }, 1500)
}
</script>

<template>
  <p class="release-meta">
    Released {{ date }} ·
    <a :href="`https://gitlab.kitware.com/vtk/vtk/-/tags/v${release.version}`">Git tag v{{ release.version }}</a> ·
    <a :href="`https://docs.vtk.org/en/latest/release_details/${series}.html`">Release notes</a> ·
    <a :href="baseUrl">Python wheels and all files</a>
  </p>
  <table class="release-files">
    <thead>
      <tr>
        <th>File</th>
        <th>Contents</th>
        <th>Size</th>
        <th>{{ checksumLabel }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="file in release.files" :key="file.name">
        <td class="name"><a :href="baseUrl + file.name">{{ file.name }}</a></td>
        <td>{{ DESCRIPTIONS[file.kind] }}</td>
        <td class="size">{{ file.size }}</td>
        <td class="checksum">
          <code :title="file.sha256 ?? file.md5">{{ (file.sha256 ?? file.md5)?.slice(0, 12) }}…</code>
          <button type="button" class="copy" @click="copyChecksum(file)">
            {{ copiedName === file.name ? 'Copied' : 'Copy' }}
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.release-meta {
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.release-files .name,
.release-files .size {
  white-space: nowrap;
}

/* Hashes are shortened on screen; the full value is in the tooltip and copied on click. */
.release-files .checksum {
  white-space: nowrap;
}

.release-files .checksum code {
  font-size: 12px;
}

.release-files .copy {
  margin-left: 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--vp-c-brand-1);
}

.release-files .copy:hover {
  text-decoration: underline;
}
</style>
