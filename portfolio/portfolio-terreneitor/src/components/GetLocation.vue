<script setup lang="js">
import { onMounted, ref } from 'vue'

const dataLocation = ref([]) // Esto es como el hook de react useState() 👀

const getLocation = async () => {
  const response = await fetch('https://geolocation.microlink.io')
  const data = await response.json()
  dataLocation.value = [data]
}

// Esto se parece a un useEffect() en React ⚛
onMounted(() => {
  getLocation()
})
</script>

<template>
  <ul>
    <h3 v-for="(location, index) in dataLocation" :key="index">
      Nos complace recibirte desde {{ location.city.name }}, {{ location.country.name }} 👋
    </h3>
  </ul>
</template>
