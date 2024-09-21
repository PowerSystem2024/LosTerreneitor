<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>

<template>
  <div>
    <h2 class="title">{{ text }}</h2>
  </div>
</template>

<style lang="css" scoped>
h2 {
  font-size: 2.6rem;
  font-weight: 800;
  text-align: center;
  margin: 50px auto;
}
</style>
