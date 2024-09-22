<script setup lang="js">
import { getLocation } from './GetLocation.vue'
import { onMounted, ref } from 'vue'

const dataLocation = ref([])

onMounted(async () => {
  const dataArray = [
    {
      city: await getLocation.city(),
      country: await getLocation.country()
    }
  ]
  dataLocation.value = dataArray
})
</script>

<template>
  <div v-if="dataLocation.length !== 0">
    <h3 v-for="(location, index) in dataLocation" :key="index">
      Nos complace recibirte desde
      <span class="gradient">{{ location.city }}, {{ location.country }}</span
      ><span class="hand">👋</span>
    </h3>
  </div>
  <div v-else>
    <h3>Cargando...</h3>
  </div>
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
