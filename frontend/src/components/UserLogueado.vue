<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'

const router = useRouter()

function logout() {
  sessionStorage.removeItem('access')
  sessionStorage.removeItem('refresh')
  router.push('/LoginAdmin')
  console.log('Sesión cerrada con éxito')
}

// mostrar registros de bibliotecas (si los hay)
const bibliotecas = ref([])

const hayRegistrosBibliotecas = computed(() => bibliotecas.value.length > 0)

onMounted(async () => {
  try {
    const response = await api.get('/bibliotecas/')
    bibliotecas.value = response.data
    console.log('Bibliotecas obtenidas con éxito:', bibliotecas.value)
  } catch (error) {
    alert('Error al obtener bibliotecas')
  }
})


// mostrar registros de autores (si los hay)
const autores = ref([])

const hayRegistrosAutores = computed(() => autores.value.length > 0)

onMounted(async () => {
  try {
    const response = await api.get('/autores/')
    autores.value = response.data
    console.log('Autores obtenidas con éxito:', autores.value)
  } catch (error) {
    alert('Error al obtener bibliotecas')
  }
})


// mostrar registros de autores (si los hay)
const libros = ref([])

const hayRegistrosLibros = computed(() => libros.value.length > 0)

onMounted(async () => {
  try {
    const response = await api.get('/libros/')
    libros.value = response.data
    console.log('Autores obtenidas con éxito:', libros.value)
  } catch (error) {
    alert('Error al obtener libros')
  }
})

</script>


<template>
    <div class="container">
        <div class="containerButtons">
            <router-link to="AddBiblioteca"><button class="btn">REGISTRAR BIBLIOTECA</button></router-link>
            <router-link to="AddAutor"><button class="btn">REGISTRAR AUTOR</button></router-link>
            <router-link to="AddLibro"><button class="btn">REGISTRAR LIBRO</button></router-link>
            <button class="btn" @click.prevent="logout">CERRAR SESIÓN</button>
        </div>
        <hr>
        <div class="containerRegistro">
            <h3>Bibliotecas:</h3>
            <p v-if="!hayRegistrosBibliotecas">No hay registros</p>
            <ul class="colorDiferente">
              <li v-for="biblioteca in bibliotecas" :key="biblioteca.id">
                <p class="registro">Nombre: {{ biblioteca.name }}</p>  
                <span>Tipo: {{ biblioteca.type_biblioteca }}</span>
        
                <div v-if="biblioteca.type_biblioteca === 'fisica'">
                  <p>Dirección: {{ biblioteca.location }}</p>
                </div>
              </li>
            </ul>
        </div>
        <div class="containerRegistro">
            <h3>Autores:</h3>
            <p v-if="!hayRegistrosAutores">No hay registros</p>
            <ul class="colorDiferente">
              <li v-for="autor in autores" :key="autor.id">
                <p class="registro">Nombre: {{ autor.name }}</p>  
                <p>Nacionalidad: {{ autor.nationality }}</p> 
              </li>
            </ul>
        </div>
        <div class="containerRegistro">
            <h3>Libros:</h3>
            <p v-if="!hayRegistrosLibros">No hay registros</p>
            <ul class="colorDiferente">
              <li v-for="libro in libros" :key="libro.id">
                <p class="registro">Título: {{ libro.title }}</p>  
                <p>Año de publicación: {{ libro.year_of_publication }}</p>
                <div class="AutoresyBibliotecas">
                  <p>Autores:</p>
                  <ul>
                    <li v-for="autor in libro.authors" :key="autor.id">{{ autor.name }}</li>
                  </ul>
                </div>
                <div class="AutoresyBibliotecas">
                  <p>Disponible en:</p>
                   <ul>
                     <li v-for="biblioteca in libro.libraries" :key="biblioteca.id">{{ biblioteca.name }}</li>
                   </ul>
                </div>
              </li>
            </ul>
        </div>
    </div>
</template>


<style scoped>

.containerButtons {
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}

.btn {
    padding: 5px 20px;
    margin: 0px 50px;
    background-color: rgb(70, 70, 141);
    color: white;
}

.containerRegistro {
    display: flex;
    flex-direction: column;
    margin: 30px 0px;
    margin-left: 30px;
}

p {
    margin-top: 3px;
}

.registro {
    margin-top: 20px;
}

.colorDiferente {
    color: rgb(149, 168, 230);
    margin-left: 17px;
}

.AutoresyBibliotecas {
  display: flex;
}

.AutoresyBibliotecas li {
  list-style-type: none;
  margin-top: 3px;
  margin-left: 4px;
}

</style>