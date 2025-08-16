<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'

const router = useRouter()
const usuario = ref({
  username: '',
  password: ''
})

const login = async () => {
  try {
    const response = await api.post('/token/', {
      username: usuario.value.username,
      password: usuario.value.password,
    })

    localStorage.setItem('access', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)

    console.log('Inicio de sesión exitoso')
    router.push('/PanelAdmin')

  } catch (error) {
    alert('Error al iniciar sesión')
  }
}

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form @submit.prevent="login">
        <h1>
          Inicia sesión como
          <br>
          administrador
        </h1>
        <div class="inputs">
          <input v-model="usuario.username" type="text" required placeholder="Nombre de usuaro">
          <input v-model="usuario.password" type="password" required placeholder="Contraseña">
          <button>Continuar</button>
        </div>
      </form>
      <p>¿No tienes una cuenta?</p>
      <router-link to="RegisterAdmin"><p id="link">Crea una aquí</p></router-link>
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
