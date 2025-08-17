<script setup>
import { ref } from "vue"
import { useRouter } from 'vue-router'
import api from "@/services/axios"

const router = useRouter()
const autor = ref({
  name: '',
  nationality: ''
})

const registrarAutor = async () => {
  try {
    const response = await api.post('/autores/', autor.value)

    console.log('Registro de autor exitoso')
    alert('Registro de autor exitoso')
    router.push('/PanelAdmin')

  } catch (error) {
    alert('Error al registrar autor')
  }
}

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form @submit.prevent="registrarAutor">
        <h1>
          Registra un autor
        </h1>
        <div class="inputs">
          <input v-model="autor.name" type="text" required placeholder="Nombre del autor">
          <input v-model="autor.nationality" type="text" required placeholder="Nacionalidad del autor">
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
  height: 550px;
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

</style>
