<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from 'vue-router'
import api from "@/services/axios"

const router = useRouter()

// mostrar datos del registro
const biblioteca = ref({
  name: '',
  type_biblioteca: '',
  location: ''
})

const valorTipoDeBiblioteca = ref('')

onMounted(async () => {
  try {
    const id = route.params.id
    const response = await api.get(`/bibliotecas/${id}/`)
    biblioteca.value = response.data
    console.log('Bibliotecas obtenidas con éxito:', biblioteca.value)

    if (biblioteca.value.type_biblioteca == 'Virtual') {
      valorTipoDeBiblioteca.value = 'Virtual'
    } else {
      valorTipoDeBiblioteca.value = 'Fisica'
    }
  } catch (error) {
    alert('Error al obtener la biblioteca')
  }
})

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form @submit.prevent="registrarBiblioteca">
        <h1>
          Edita esta biblioteca
        </h1>
        <div class="inputs">
          <input v-model="biblioteca.name" type="text" required>
          <div class="checkInput">
            <input type="radio" id="virtual" name="tipo" value="virtual" v-model="valorTipoDeBiblioteca">
            <label for="virtual">Virtual</label>
          </div>
          <div class="checkInput">
            <input type="radio" id="fisica" name="tipo" value="fisica" v-model="valorTipoDeBiblioteca">
            <label for="fisica">Física</label>
          </div>
          <input v-model="biblioteca.location" v-if="biblioteca.type_biblioteca === 'fisica'" type="text" required placeholder="Ubicación">
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

.checkInput {
    display: flex;
    justify-content: center;
}

label {
    margin-left: 5px;
    margin-top: 2px;
}

.checkInput input:hover, label:hover {
  cursor: pointer;
}

</style>
