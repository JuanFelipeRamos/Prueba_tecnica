<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function logout() {
  sessionStorage.removeItem('access')
  sessionStorage.removeItem('refresh')
  router.push('/LoginAdmin')
  console.log('Sesión cerrada con éxito')
}

</script>


<template>
    <div class="container">
        <div class="containerButtons">
            <router-link to="AddBiblioteca"><button class="btn">BIBLIOTECAS</button></router-link>
            <button class="btn">AUTORES</button>
            <button class="btn">LIBROS</button>
            <button class="btn" @click.prevent="logout">CERRAR SESIÓN</button>
        </div>
        <hr>
        <div class="containerRegistro">
            <h3>Bibliotecas:</h3>
            <p>No hay registros</p>
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
    margin: 0px 70px;
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

</style>