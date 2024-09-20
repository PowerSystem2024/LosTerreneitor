<script setup lang="js">
import GroupMembers from './components/GroupMembers.vue'
import HeroComponent from './components/HeroComponent.vue'
import MainNav from './components/MainNav.vue'
import MainFooter from '@/components/MainFooter.vue'
import MainProyects from '@/components/MainProyects.vue'
import SectionTitle from './components/SectionTitle.vue'
</script>

<template>
  <header>
    <MainNav />
  </header>
  <section class="wrapper">
    <HeroComponent title="Terreneitor" />
  </section>
  <section class="wrapper">
    <SectionTitle title="Proyectos" />
    <MainProyects />
  </section>
  <section class="wrapper">
    <SectionTitle title="Integrantes del Grupo" />
    <GroupMembers />
  </section>
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
