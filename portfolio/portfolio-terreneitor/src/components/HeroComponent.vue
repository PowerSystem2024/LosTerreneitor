<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div>
    <h1 class="main-title">{{ msg }}</h1>
    <h3>
      Bienvenidos al portafolio web del grupo Los Terreneitor Tecnicatura Universitaria en
      Programación Cohorte 2024 UTN-FRSR.
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}
</style>
