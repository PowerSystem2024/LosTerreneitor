import { ref, onMounted, onUnmounted } from 'vue'

export function useMatchMedia(query) {
  const matches = ref(false)
  let mediaQuery

  const updateMatches = (e) => {
    matches.value = e.matches
  }

  onMounted(() => {
    mediaQuery = window.matchMedia(query)
    matches.value = mediaQuery.matches
    mediaQuery.addEventListener('change', updateMatches)
  })

  onUnmounted(() => {
    mediaQuery.removeEventListener('change', updateMatches)
  })

  return matches
}
