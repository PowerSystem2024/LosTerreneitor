<script setup lang="js">
import GetLocation from './components/GetLocation.vue'
import HeroComponent from './components/HeroComponent.vue'
import MainNav from './components/MainNav.vue'
import MainFooter from '@/components/MainFooter.vue'
import MainProyects from '@/components/MainProyects.vue'
</script>

<template>
  <header>
    <MainNav />
  </header>

  <div class="wrapper">
    <HeroComponent msg="Terreneitor" />
    <GetLocation />
    <MainProyects />
  </div>
  <MainFooter />
</template>

<style lang="css" scoped>
.wrapper {
  max-width: 872px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  margin: 25px auto;
}
</style>
