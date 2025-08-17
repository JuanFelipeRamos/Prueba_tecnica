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

const hayRegistros = computed(() => bibliotecas.value.length > 0)

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
    <div class="container">
        <div class="containerButtons">
            <router-link to="AddBiblioteca"><button class="btn">REGISTRA BIBLIOTECAS</button></router-link>
            <button class="btn">REGISTRA AUTORES</button>
            <button class="btn">REGISTRA LIBROS</button>
            <button class="btn" @click.prevent="logout">CERRAR SESIÓN</button>
        </div>
        <hr>
        <div class="containerRegistro">
            <h3>Bibliotecas:</h3>
            <p v-if="!hayRegistros">No hay registros</p>
            <ul class="colorDiferente">
              <li v-for="biblioteca in bibliotecas" :key="biblioteca.id">
                <p class="registroBibliotec">Nombre: {{ biblioteca.name }}</p>  
                <span>Tipo: {{ biblioteca.type_biblioteca }}</span>
        
                <div v-if="biblioteca.type_biblioteca === 'fisica'">
                  <p>Dirección: {{ biblioteca.location }}</p>
                </div>
              </li>
            </ul>
        </div>
        <div class="containerRegistro">
            <h3>Autores:</h3>
            <p>No hay registros</p>
        </div>
        <div class="containerRegistro">
            <h3>Libros:</h3>
            <p>No hay registros</p>
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
    margin-left: 10px;
}

p {
    margin-top: 3px;
}

.registroBibliotec {
    margin-top: 20px;
}

.colorDiferente {
    color: rgb(149, 168, 230);
}

</style>