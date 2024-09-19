<script setup lang="js">
import { ref } from 'vue'

const proyects = ref([])
const items = [
  {
    name: 'Proyecto 1',
    link: 'https://elproyecto.qui',
    description: 'Soy la descripción del proyecto'
  },
  {
    name: 'Proyecto 1',
    link: 'https://elproyecto.qui',
    description: 'Soy la descripción del proyecto'
  },
  {
    name: 'Proyecto 1',
    link: 'https://elproyecto.qui',
    description: 'Soy la descripción del proyecto'
  }
]
proyects.value = items
</script>

<template>
  <div v-for="(proyect, index) in proyects" :key="index">
    <h2>{{ proyect.name }}</h2>
    <p>{{ proyect.description }}</p>
    <a :href="proyect.link">Link</a>
  </div>
</template>

<style lang="css" scoped>
div {
  display: grid;
  justify-content: center;
  margin: 30px auto;
}
</style>
