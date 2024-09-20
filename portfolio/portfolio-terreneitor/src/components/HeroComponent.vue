<script setup lang="ts">
import GetLocation from './GetLocation.vue'
defineProps<{
  title: string
}>()
</script>

<template>
  <div class="hero">
    <h1 class="main-title">{{ title }}</h1>
    <article>
      <h3>
        Bienvenidos al portafolio web del grupo Los Terreneitor de la Tecnicatura Universitaria en
        Programación Cohorte 2024 UTN-FRSR.
      </h3>
    </article>
    <GetLocation />
  </div>
</template>

<style scoped>
.hero {
  margin: 24px 0;
}

article {
  max-width: 872px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 0 auto;
  text-wrap: pretty;
}

.main-title {
  margin: 50px 0;
  font-size: 6rem;
  font-weight: 800;
  text-decoration: none;
  color: transparent;
  transition: 0.4s;
  padding: 3px;
  display: flex;
  place-content: center;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: rgb(189, 139, 0);
  text-shadow: 0 0 10px rgb(189, 139, 0);
}

@media (max-width: 700px) {
  .main-title {
    font-size: 3.8rem;
  }
}

h3 {
  padding: 4px;
  text-align: center;
  font-size: 2.2rem;
  font-weight: 700;
}
</style>
