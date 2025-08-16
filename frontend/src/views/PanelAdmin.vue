<script setup>
import { ref } from 'vue'
import UserLogueado from '@/components/UserLogueado.vue'

const logueado = ref(false)
const token = sessionStorage.getItem('access')

if (token) {
    logueado.value = true
    console.log("Acceso consedido al panel de admin.")
} else {
    console.log("Acceso denegado al panel de admin.")
}

</script>


<template>
    <div class="container">
        <div v-if="logueado">
            <UserLogueado />
        </div>
        <div v-else class="noAccess">
            <h1>Debes iniciar sesión como admin para tener acceso al panel</h1>
            <router-link to="LoginAdmin"><p>Inicia sesión aquí</p></router-link>
        </div>
    </div>
</template>


<style scoped>

.noAccess {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 300px;
    flex-direction: column;
}

p {
    text-decoration: none;
    color: rgb(135, 161, 211);
    font-size: 23px;
}

</style>