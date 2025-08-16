<script setup>

</script>

<template>
  <div class="container">
    <div class="containerformilario">
      <form>
        <h1>
          Registra una biblioteca
        </h1>
        <div class="inputs">
          <input type="text" required placeholder="Nombre de la biblioteca">
          <div class="checkInput">
            <input type="checkbox"><p class="pCheck">Virtual</p>
          </div>
          <div class="checkInput">
            <input type="checkbox"><p class="pCheck">Física</p>
          </div>
          <input type="text" required placeholder="Ubicación">
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

.pCheck {
    margin-left: 5px;
    margin-top: 2px;
}

</style>
