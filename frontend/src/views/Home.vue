<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '../services/axios'

// mostrar registros de libros (si los hay)
const libros = ref([])

const hayRegistrosLibros = computed(() => libros.value.length > 0)

onMounted(async () => {
  try {
    const response = await api.get('/libros/')
    libros.value = response.data
    console.log('Libros obtenidas con éxito:', libros.value)
  } catch (error) {
    alert('Error al obtener libros')
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
    alert('Error al obtener libros')
  }
})

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

</script>


<template>
    <div>
        <div class="containerH1">
            <h1>BiblioTEC</h1>
        </div>
        <hr>
        <h2>Libros:</h2>
        <div class="containerTargetas">
            <p v-if="!hayRegistrosLibros" class="sinRegistros">No hay registros</p>
            <div class="targeta" v-for="libro in libros" :key="libro.id">
                <div class="gris">
                    <p class="colorTitle"><strong>{{ libro.title }}</strong></p>
                </div>
                <div class="blanco">
                    <p><strong>Publicado en:</strong> 
                        {{ libro.year_of_publication }}
                    </p>
                </div>
                <div class="gris">
                    <p><strong>Autores:</strong></p>
                    <ul>
                      <li v-for="autor in libro.authors" :key="autor.id">{{ autor.name }}</li>
                    </ul>
                </div>
                <div class="blanco">
                    <p><strong>Disponible en:</strong></p>
                     <ul>
                       <li v-for="biblioteca in libro.libraries" :key="biblioteca.id">{{ biblioteca.name }}</li>
                     </ul>
                </div>
            </div>
        </div>
        <hr class="hr">

        <h2>Autores:</h2>
        <div class="containerTargetas">
            <p v-if="!hayRegistrosAutores" class="sinRegistros">No hay registros</p>
            <div class="targeta" v-for="autor in autores" :key="autor.id">
                <div class="gris">
                    <p class="colorTitle"><strong>{{ autor.name }}</strong></p>
                </div>
                <div class="blanco">
                    <p><strong>Nacionalidad:</strong> {{ autor.nationality }}</p>
                </div>
                <div class="gris">
                    <p>Ver libros...</p>
                </div>
            </div>
        </div>
        <hr class="hr">

        <h2>Bibliotecas:</h2>
        <div class="containerBibliotecas">
            <p v-if="!hayRegistrosBibliotecas" class="sinRegistros">No hay registros</p>
            <div v-for="biblioteca in bibliotecas" :key="biblioteca.id">
                <ul class="biblioteca">
                    <router-link :to="`/LibrosdeBiblioteca/${biblioteca.id}`"><li>{{ biblioteca.name }}</li></router-link>
                </ul>
            </div>
        </div>
    </div>
</template>


<style scoped>

.containerH1 {
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}

.hr {
    margin-top: 28px;
}

h2 {
    margin-top: 20px;
}

.containerTargetas {
    display: flex;
    justify-content: center;
}

.sinRegistros {
    font-size: 17px;
}

.targeta {
    flex-direction: column;
    width: 20%;
    margin: 20px 80px 0px 80px;
    border: solid 2px rgb(118, 125, 158);
    border-radius: 5px;
}

.targeta p, .targeta li {
    font-size: 18px;
    margin: 10px 0px;
    list-style-type: none;
    text-align: center;
}

.gris {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: rgb(70, 70, 70);
    width: 100%;
}

.colorTitle {
    color: rgb(0, 0, 34);
}

.blanco {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: rgb(92, 92, 92);
    width: 100%;
}

.biblioteca {
    margin: 10px 0px 10px 22px;
}

.biblioteca li {
    color: white;
}

.containerBibliotecas {
    display: flex;
    flex-direction: column;
    height: 130px;
}

</style>