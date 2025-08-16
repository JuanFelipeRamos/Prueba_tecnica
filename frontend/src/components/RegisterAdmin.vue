<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import api from '../services/axios';

const router = useRouter()
const usuario = ref({
  username: "",
  first_name: "",
  last_name: "",
  password: "",
  key_admin: ""
});

const registrarUsuario = async (e) => {
  e.preventDefault()

  try {
    const response = await api.post('/admins/registro/', usuario.value)
    alert('Registro de usuario administrador exitoso, ya puedes iniciar sesión.')

    usuario.value = {
      username: '',
      first_name: '',
      last_name: '',
      password: '',
      key_admin: ''
    }

    router.push('/LoginAdmin')
  } catch (error) {
    alert('Error al registrar el usuario administrador.')
    console.error('Error al registrar:', error)
  }
}

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form @submit.prevent="registrarUsuario">
        <h1>
          Regístrate como
          <br>
          administrador
        </h1>
        <div class="inputs">
          <input v-model="usuario.username" type="text" required placeholder="Nombre de usuaro">
          <input v-model="usuario.first_name" type="text" required placeholder="Nombres">
          <input v-model="usuario.last_name" type="text" placeholder="Apellidos">
          <input v-model="usuario.password" type="password" required placeholder="Contraseña">
          <input v-model="usuario.key_admin" type="password" required placeholder="Clave de acceso para admin">
          <button>Continuar</button>
        </div>
      </form>
      <p>Ya tienes una cuenta?</p>
      <router-link to="LoginAdmin"><p id="link">Inisia sesión aquí</p></router-link>
    </div>
  </div>
</template>


<style scoped>

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 600px;
}

.containerformilario {
  border: solid rgb(41, 41, 90) 2px;
  border-radius: 8px;
  padding: 50px 48px;
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
