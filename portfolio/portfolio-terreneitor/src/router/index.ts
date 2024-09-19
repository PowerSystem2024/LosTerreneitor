import HeroComponent from '@/components/HeroComponent.vue'
import AboutView from '@/views/AboutView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HeroComponent
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    }
  ]
})

export default router
