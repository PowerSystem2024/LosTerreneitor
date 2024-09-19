<script setup lang="js">
import { AlignRight, X } from 'lucide-vue-next'
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
    name: 'Contacto',
    path: '/contact'
  },
  {
    name: 'Proyectos',
    path: '#proyects'
  }
]
items.value = navItems

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<template>
  <nav>
    <img
      alt="Logo Terreneitor"
      class="logo"
      src="@/assets/logo-terreneitor-removebg.png"
      width="75"
      height="45"
    />

    <button class="menu-btn" @click="toggleMenu">
      <AlignRight class="menu-icon" />
      <X class="x-icon" />
    </button>

    <aside :class="{ open: isMenuOpen }">
      <li v-for="(item, index) in navItems" :key="index">
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
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--color-border);
  font-size: 12px;
  text-align: center;
  align-items: center;
  justify-content: space-between;
  z-index: 99;
  padding: 0 1rem;
}

aside {
  display: flex;
  margin-right: 2rem;
  gap: 12px;
}

aside li {
  list-style: none;
}

a {
  color: #ddd;
  text-decoration: none;
  font-size: 1rem;
}

.menu-btn {
  display: none;
  border: none;
  background-color: transparent;
  z-index: 99;
}

.menu-icon {
  color: #ddd;
}

.x-icon {
  display: none;
}

@media (max-width: 700px) {
  .menu-btn {
    display: flex;
  }

  aside {
    position: absolute;
    top: 0px;
    left: 0;
    width: 100%;
    height: 100dvh;
    place-content: center;
    background-color: rgba(112, 112, 112, 0.696);
    backdrop-filter: blur(10px);
    flex-direction: column;
    padding: 1rem;
    display: none;
  }

  aside.open {
    display: flex;
  }

  aside.open .menu-icon {
    display: none;
  }

  aside li {
    margin-bottom: 1rem;
  }
}
</style>
