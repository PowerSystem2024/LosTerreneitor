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
    <span class="gradient">{{ location.city.name }}, {{ location.country.name }}</span
    ><span class="hand">👋</span>
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
}

.gradient {
  background-image: linear-gradient(260deg, var(--purple), var(--green));
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 700;
}

.hand {
  display: inline-block;
  margin-left: 4px;
  animation: wave 1.3s infinite alternate;
  transform: rotate(35deg) translateY(-3px);
}

@keyframes wave {
  to {
    transform: rotate(8deg);
  }
}

@media (max-width: 700px) {
  h3,
  span {
    font-size: 1.5rem;
  }
}
</style>
