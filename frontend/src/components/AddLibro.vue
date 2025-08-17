<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from 'vue-router'
import api from "@/services/axios"

const router = useRouter()
const libro = ref({
  title: '',
  year_of_publication: 1990,
  authors_ids: [],
  libraries_ids: []
})

const registrarLibro = async () => {
  try {
    const response = await api.post('/libros/', libro.value)

    console.log('Registro de libro exitoso')
    alert('Registro de libro exitoso')
    router.push('/PanelAdmin')
    console.log(libro.value)

  } catch (error) {
    alert('Error al registrar libro')
  }
}

// mostrar opciones de autores para seleccionar
const autores = ref([])

onMounted(async () => {
  try {
    const response = await api.get('/autores/')
    autores.value = response.data
    console.log('Autores obtenidas con éxito:', autores.value)
  } catch (error) {
    alert('Error al obtener bibliotecas')
  }
})

// mostrar opciones de autores para seleccionar
const bibliotecas = ref([])

onMounted(async () => {
  try {
    const response = await api.get('/bibliotecas/')
    bibliotecas.value = response.data
    console.log('Autores obtenidas con éxito:', bibliotecas.value)
  } catch (error) {
    alert('Error al obtener bibliotecas')
  }
})

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form @submit.prevent="registrarLibro">
        <h1>
          Registra un libro
        </h1>
        <div class="inputs">
          <input v-model="libro.title" type="text" required placeholder="Título del libro">
          <label>Selecciona el año de publicación</label>
          <input v-model="libro.year_of_publication" type="number" min=1450 max=2025 step="1" required>
          <!--Para seleccionar autor/es-->
          <label>Selecciona uno o varios autores</label>
          <select v-model="libro.authors_ids" multiple required>
            <option v-for="autor in autores" :key="autor.id" :value="autor.id">{{ autor.name }}</option>
          </select>
          <!--Para seleccionar biblioteca/s-->
          <label>Selecciona una o varias bibliotecas</label>
          <select v-model="libro.libraries_ids" multiple required>
            <option v-for="biblioteca in bibliotecas" :key="biblioteca.id" :value="biblioteca.id">{{ biblioteca.name }}</option>
          </select>
          <button>Continuar</button>
        </div>
      </form>
      <router-link to="PanelAdmin"><p id="link">Volver</p></router-link>
    </div>
  </div>
</template>


<style scoped>

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 590px;
}

.containerformilario {
  border: solid rgb(41, 41, 90) 2px;
  border-radius: 8px;
  padding: 50px 38px;
  background-color: rgb(27, 27, 85);
  text-align: center;
}

h1 {
  text-align: center;
  font-size: 30px;
  margin-bottom: 14px;
}

.inputs {
  display: flex;
  flex-direction: column;
}

input {
  padding: 7px;
  margin: 6px 0px;
}

button {
  padding: 6px;
  margin-top: 7px;
  background-color: rgb(70, 70, 141);
  color: white;
}

form {
  margin-bottom: 15px;
}

p {
  font-size: 18px;
}

#link {
  text-decoration: none;
  color: white;
}

#link:hover {
  color: rgb(139, 139, 139);
}

label {
    margin-top: 14px;
}

select{
    height: 32px;
}

</style>
