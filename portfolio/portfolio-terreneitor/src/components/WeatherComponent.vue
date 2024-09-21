<script setup lang="js">
import { onMounted, ref } from 'vue'

import { apiKey, kelvintoCelsius, getWeatherIcon, mapCondition } from './constants.vue'
import { getLocation } from './GetLocation.vue';

const dataAPI = ref([])

const getDataWeather = async () => {
  const lat = await getLocation.lat()
  const lon = await getLocation.lon()
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`
  const res = await fetch(url)
  const data = res.json()
  return data
}

onMounted(async () => {
  dataAPI.value[0] = await getDataWeather()
})
</script>

<template>
  <section>
    <table class="data-weather" v-for="(data, index) in dataAPI" :key="index" cellspacing="collapse" cellpadding="0">
      <div v-if="data.name === ''">
      <h2>Cargando datos del clima...</h2>
      </div>
        <div v-else class="table-title">
          <h2>El clima en {{ data.name }}</h2>
          <img :src="getWeatherIcon(data.weather[0].icon)" alt="Icono del Clima" class="image-icon" />
        </div>
        <thead>
          <tr>
          <th>Temperatura</th>
          <th>Humedad</th>
          <th>Temp. Máxima</th>
          <th>Temp. Mínima</th>
          <th>Condición</th>
          </tr>
        <tbody>
          <tr>
            <td>{{ kelvintoCelsius(data.main.temp).toFixed(1) }}°</td>
            <td>{{ data.main.humidity }}%</td>
            <td>{{ kelvintoCelsius(data.main.temp_max).toFixed(1) }}°</td>
            <td>{{ kelvintoCelsius(data.main.temp_min).toFixed(1) }}°</td>
            <td>{{ mapCondition(data.weather[0].description) }}</td>
          </tr>
        </tbody>
      </thead>
    </table>
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

.table-title {
  display: flex;
  justify-content: center;
  align-items: center;
}

h2 {
  text-align: center;
}

.data-weather {
  display: flex;
  flex-direction: column;
}

table {
  margin: 50px auto;
}

th, td {
  padding: 4px;
  border: 1px solid var(--color-border);
}
</style>
