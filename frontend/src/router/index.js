import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import LoginAdmin from '@/components/LoginAdmin.vue'
import RegisterAdmin from '@/components/RegisterAdmin.vue'
import PanelAdmin from '@/views/PanelAdmin.vue'
import UserLogueado from '@/components/UserLogueado.vue'
import AddBiblioteca from '@/components/AddBiblioteca.vue'

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

    {
      path: '/UserLogueado',
      name: 'userLogueado',
      component: UserLogueado
    },

    {
      path: '/AddBiblioteca',
      name: 'addBiblioteca',
      component: AddBiblioteca
    },

  ],
})

export default router
