<script setup lang="ts">
import { onMounted, ref } from 'vue'

interface LocationData {
  city: {
    name: string
  }
  country: {
    name: string
  }
}

const dataLocation = ref<LocationData[]>([])

const getLocation = async () => {
  const response = await fetch('https://geolocation.microlink.io')
  const data = await response.json()
  dataLocation.value = [data as LocationData]
}

onMounted(() => {
  getLocation()
})
</script>

<template>
  <h3 v-for="(location, index) in dataLocation" :key="index">
    Nos complace recibirte desde
    <span class="gradient">{{ location.city.name }}, {{ location.country.name }}</span> 👋
  </h3>
</template>

<style lang="css" scoped>
h3 {
  margin: 24px auto;
  text-align: center;
  font-size: 2.2rem;
  font-weight: 700;
  padding: 4px;
}
span {
  font-size: 2.2rem;
  font-weight: 700;
  color: rgb(189, 139, 0);
}
.gradient {
  background-image: linear-gradient(260deg, var(--purple), var(--green));
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}
</style>
