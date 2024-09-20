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
  -webkit-text-stroke-color: var(--color-text);
  -webkit-box-reflect: below -85px linear-gradient(to bottom, transparent, rgba(222, 222, 222, 0.15));
  background-image: linear-gradient(260deg, var(--purple), var(--green));
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media (max-width: 700px) {
  .main-title {
    font-size: 3.8rem;
    -webkit-box-reflect: below -50px linear-gradient(to bottom, transparent, rgba(222, 222, 222, 0.15));
    background-image: linear-gradient(260deg, var(--purple), var(--green));
  }

  h3 {
    font-size: 1.5rem;
  }
}

h3 {
  padding: 4px;
  text-align: center;
  font-size: 2.2rem;
  font-weight: 800;
}
</style>
