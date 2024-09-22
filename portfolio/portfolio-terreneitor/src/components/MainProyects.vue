<script setup lang="js">
import { proyectsItems } from './constants.vue'
import { Github, ArrowUpRight } from 'lucide-vue-next'
import { useMatchMedia } from '../hook/UseMatchMedia'

const isMobile = useMatchMedia('(max-width: 700px)')
</script>

<template>
  <section v-if="!isMobile" class="proyect-grid">
    <div class="proyect-container" v-for="(proyect, index) in proyectsItems" :key="index">
      <article class="proyect">
        <img :src="proyect.img" width="100%" height="auto" :alt="proyect.name" />
        <h2>{{ proyect.name }}</h2>
        <p class="description">{{ proyect.description }}</p>
        <aside>
          <a :href="proyect.code">
            <Github class="github-icon" />
            Code
          </a>
          <a :href="proyect.link">
            Link
            <ArrowUpRight class="arrow-up-rigth-icon" />
          </a>
        </aside>
      </article>
    </div>
  </section>
  <section v-else class="mobile-scroll">
    <div class="proyect-container" v-for="(proyect, index) in proyectsItems" :key="index">
      <article class="proyect">
        <img :src="proyect.img" width="100%" height="auto" :alt="proyect.name" />
        <h2>{{ proyect.name }}</h2>
        <p class="description">{{ proyect.description }}</p>
        <aside>
          <a :href="proyect.code">
            <Github class="github-icon" />
            Code
          </a>
          <a :href="proyect.link">
            Link
            <ArrowUpRight class="arrow-up-rigth-icon" />
          </a>
        </aside>
      </article>
    </div>
  </section>
</template>

<style lang="css" scoped>
.proyect-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  margin: 24px 12px;
  gap: 16px;
  width: 100%;
}

.proyect-container {
  background-color: var(--color-card);
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 9;
}

.mobile-scroll {
  display: flex;
  overflow-x: auto;
  gap: 16px;
  padding: 16px;
  scroll-snap-type: x mandatory;
}

.mobile-scroll .proyect-container {
  flex: 0 0 auto;
  width: 80%;
  scroll-snap-align: start;
}

.proyect {
  padding: 16px;
  color: #333;
  border-radius: 10px;
}

h2 {
  font-weight: 600;
  color: var(--color-text);
}

img {
  border-radius: 10px;
}

.description {
  margin: 10px auto;
  height: 80px;
  color: var(--color-text);
}

aside {
  margin: 10px auto 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

aside a {
  text-decoration: none;
  align-items: center;
  color: var(--color-text);
}

aside a:hover {
  opacity: 0.6;
  color: royalblue;
}

.github-icon,
.arrow-up-rigth-icon {
  width: 16px;
  height: 16px;
  transform: translateY(2px);
}
</style>
