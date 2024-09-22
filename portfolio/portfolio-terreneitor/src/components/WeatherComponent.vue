<script setup lang="js">
import { onMounted, ref } from 'vue'

import { kelvintoCelsius, getWeatherIcon, mapCondition } from './constants.vue'
import { getLocation } from './GetLocation.vue'

const dataAPI = ref([])

const getDataWeather = async () => {
  const lat = await getLocation.lat()
  const lon = await getLocation.lon()
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=2232101b7a4c133da51de8620fc86462`
  const res = await fetch(url)
  const data = await res.json()
  return data
}

onMounted(async () => {
  dataAPI.value[0] = await getDataWeather()
})
</script>

<template>
  <section>
    <div v-for="(data, index) in dataAPI" :key="index" class="weather-container">
      <div class="title">
        <h2>El clima en {{ data.name }}</h2>
        <img :src="getWeatherIcon(data.weather[0].icon)" alt="Icono del Clima" class="image-icon" />
        <span>{{ kelvintoCelsius(data.main.temp).toFixed(1) }}°</span>
      </div>
      <div class="data-weather-grid">
        <div class="grid-item">
          <strong>Condición:</strong>
          <span>{{ mapCondition(data.weather[0].description) }}</span>
        </div>
        <div class="grid-item">
          <strong>Sensación:</strong>
          <span>{{ kelvintoCelsius(data.main.feels_like).toFixed(1) }}°</span>
        </div>
        <div class="grid-item">
          <strong>Humedad:</strong>
          <span>{{ data.main.humidity }}%</span>
        </div>
        <div class="grid-item">
          <strong>Viento:</strong>
          <span>{{ data.wind.speed }}km/h</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="css" scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0 auto;
  font-family: monospace;
}

.weather-container {
  margin: 50px auto;
}

.title {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

h2 {
  text-align: center;
}

.image-icon {
  width: 65px;
  height: 65px;
}

.data-weather-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 8px;
  margin: 0 auto;
  padding: 8px;
  border: 1px solid var(--color-border);
  border-radius: 10px;
}

.grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4px;
  border: 1px solid var(--color-border);
  border-radius: 10px;
  text-align: center;
}

strong {
  margin-bottom: 5px;
}
</style>
