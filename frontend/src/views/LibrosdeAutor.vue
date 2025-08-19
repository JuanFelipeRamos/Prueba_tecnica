<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/axios'

const route = useRoute() 
const autor = ref({ name: '', libros: [] })

onMounted(async () => {
  try {
    const id = route.params.id
    const response = await api.get(`/autores/${id}/`)
    autor.value = response.data
    console.log('Autor obtenido con éxito:', autor.value)
  } catch (error) {
    alert('Error al obtener el autor')
  }
})
</script>

<template>
  <div>
    <div class="containerH1">
      <h1>BiblioTEC</h1>
    </div>
    <hr>

    <h2 v-if="autor.name">
      Libros del autor <strong>{{ autor.name }}</strong>:
    </h2>
    <p v-else class="sinRegistros">No hay registros</p>

    <ul>
      <li v-for="libro in autor.libros" :key="libro.id">
        {{ libro.title }}
      </li>
    </ul>
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

.sinRegistros {
    font-size: 17px;
}

.biblioteca {
    margin: 10px 0px 10px 22px;
}

.containerBibliotecas {
    display: flex;
    flex-direction: column;
    height: 130px;
}

li {
    margin-top: 8px;
    margin-left: 22px;
}

</style>