<script setup lang="js">
import GetLocation from './components/GetLocation.vue'
import HeroComponent from './components/HeroComponent.vue'
import MainNav from './components/MainNav.vue'
</script>

<template>
  <header>
    <MainNav />
  </header>

  <div class="wrapper">
    <HeroComponent msg="Terreneitor" />
    <GetLocation />
  </div>
</template>
