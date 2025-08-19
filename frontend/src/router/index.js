import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import LoginAdmin from '@/components/LoginAdmin.vue'
import RegisterAdmin from '@/components/RegisterAdmin.vue'
import PanelAdmin from '@/views/PanelAdmin.vue'
import UserLogueado from '@/components/UserLogueado.vue'
import AddBiblioteca from '@/components/AddBiblioteca.vue'
import AddAutor from '@/components/AddAutor.vue'
import AddLibro from '@/components/AddLibro.vue'
import EditBiblioteca from '@/components/EditBiblioteca.vue'
import LibrosdeBiblioteca from '@/views/LibrosdeBiblioteca.vue'
import LibrosdeAutor from '@/views/LibrosdeAutor.vue'

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

    {
      path: '/AddAutor',
      name: 'addAutor',
      component: AddAutor
    },

    {
      path: '/AddLibro',
      name: 'addLibro',
      component: AddLibro
    },

    {
      path: '/EditBiblioteca',
      name: 'editBiblioteca',
      component: EditBiblioteca
    },

    {
      path: '/LibrosdeBiblioteca/:id',
      name: 'librosdeBiblioteca',
      component: LibrosdeBiblioteca
    },

    {
      path: '/LibrosdeAutor/:id',
      name: 'librosdeAutor',
      component: LibrosdeAutor
    },

  ],
})

export default router
