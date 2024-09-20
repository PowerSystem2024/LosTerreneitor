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
    <div class="logo-container">
      <img
        alt="Logo Terreneitor"
        class="logo"
        src="@/assets/logo-terreneitor-removebg.png"
        width="80"
        height="50"
      />
      <span>BETA</span>
    </div>
    <button class="menu-btn" @click="toggleMenu">
      <AlignRight v-if="!isMenuOpen" class="menu-icon" />
      <X v-if="isMenuOpen" class="x-icon" />
    </button>

    <aside :class="{ open: isMenuOpen }">
      <li v-for="(item, index) in navItems" :key="index">
        <RouterLink class="link" :to="item.path">{{ item.name }}</RouterLink>
      </li>
      <footer v-if="isMenuOpen">
        <p>&copy;Terreneitor - UTN-FRSR {{ new Date().getFullYear() }}</p>
      </footer>
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

.logo-container {
  display: flex;
  align-items: center;
}

.logo:hover {
  transform: scale(1.1);
  transition: transform 0.3s ease-in-out;
}

.logo-container span {
  background-color: rgba(189, 139, 0, 0.659);
  border: 1px solid rgba(255, 166, 0, 0.782);
  padding: 2px 6px;
  border-radius: 50px;
  font-weight: 600;
  font-size: 10px;
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
  padding: 2px 8px 3px 8px;
}

a:hover {
  opacity: 0.8;
  background-color: rgba(97, 97, 97, 0.5);
  border-radius: 10px;
  transition: 0.3s ease-in-out;
  color: rgb(189, 139, 0);
}

.menu-btn {
  display: none;
  border: none;
  background-color: transparent;
  z-index: 99;
}

.menu-icon,
.x-icon {
  color: #ddd;
}

.x-icon {
  transform: rotate(-45deg);
  animation: spin 0.4s linear both;
  transition: transform 0.3s;
}

@keyframes spin {
  to {
    transform: rotate(90deg);
  }
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
    background-color: rgba(32, 29, 29, 0.89);
    backdrop-filter: blur(10px);
    flex-direction: column;
    padding: 1rem;
    display: none;
  }

  aside.open {
    display: flex;
  }

  aside.open .link {
    font-size: 1.5rem;
    font-weight: 600;
  }

  aside.open footer p {
    font-size: 1rem;
    font-weight: 600;
    color: rgb(189, 139, 0);
  }

  aside li {
    margin-bottom: 1rem;
  }
}
</style>
