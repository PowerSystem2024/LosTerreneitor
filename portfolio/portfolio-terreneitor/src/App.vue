<script setup lang="js">
import GroupMembers from './components/GroupMembers.vue'
import HeroComponent from './components/HeroComponent.vue'
import MainNav from './components/MainNav.vue'
import MainFooter from '@/components/MainFooter.vue'
import MainProyects from '@/components/MainProyects.vue'
import SectionTitle from './components/SectionTitle.vue'
import UnderConstruction from './components/UnderConstruction.vue'
import WeatherComponent from './components/WeatherComponent.vue'
</script>

<template>
  <header>
    <MainNav />
  </header>
  <section class="wrapper">
    <HeroComponent />

    <SectionTitle text="Proyectos" />
    <MainProyects />

    <SectionTitle text="Integrantes del Grupo" />
    <GroupMembers />
    <UnderConstruction msg="Esta web se encuentra en construcción..." />
  </section>
  <WeatherComponent />
  <MainFooter />
</template>

<style lang="css" scoped>
.wrapper {
  max-width: 872px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 50px auto;
}
</style>
