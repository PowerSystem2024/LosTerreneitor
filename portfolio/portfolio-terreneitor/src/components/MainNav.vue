<script setup lang="js">
import { ref } from 'vue'
const items = ref([])

const navItems = [
  {
    name: 'Inicio',
    path: '/'
  },
  {
    name: 'Acerca',
    path: '/about'
  },
  {
    name: 'Contaco',
    path: '/contact'
  },
  {
    name: 'Proyectos',
    path: '#proyects'
  }
]
items.value = navItems
</script>

<template>
  <nav>
    <img
      alt="Vue logo"
      class="logo"
      src="@/assets/logo-terreneitor-removebg.png"
      width="85"
      height="55"
    />
    <aside>
      <li v-for="(item, index) in items" :key="index">
        <RouterLink :to="item.path">{{ item.name }}</RouterLink>
      </li>
    </aside>
  </nav>
</template>

<style scoped>
nav {
  position: fixed;
  display: flex;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background-color: rgba(97, 97, 97, 0.5);
  border-bottom: 1px solid var(--color-border);
  font-size: 12px;
  text-align: center;
  align-items: center;
  justify-content: space-between;
}
aside {
  display: flex;
  margin-right: 2rem;
  gap: 12px;
}

aside li {
  text-decoration: none;
  list-style: none;
}
a {
  color: #ddd;
  text-decoration: none;
  font-size: 1rem;
}
</style>
