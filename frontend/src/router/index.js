import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import LoginAdmin from '@/components/LoginAdmin.vue'
import RegisterAdmin from '@/components/RegisterAdmin.vue'
import PanelAdmin from '@/views/PanelAdmin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },

    {
      path: '/LoginAdmin',
      name: 'loginAdmin',
      component: LoginAdmin
    },

    {
      path: '/RegisterAdmin',
      name: 'registerAdmin',
      component: RegisterAdmin
    },

    {
      path: '/PanelAdmin',
      name: 'panelAdmin',
      component: PanelAdmin
    },

  ],
})

export default router
