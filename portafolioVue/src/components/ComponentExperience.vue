<script setup>
import icono1 from '/src/assets/ecommerce.svg';
import icono2 from '/src/assets/config.svg';

import { ref } from 'vue';
const titulo = 'Desarrolladores Full Stack';
const fecha = 'Desde Enero 2023 / Julio 2024';
const experiencias = ref([
    { id: 1, src: icono1, parrafo: 'Creamos un e-commerce que solucionó e incrementó las ventas de nuestro cliente, aplicamos nuestros conocimientos adquiridos en la TUP.' },
    { id: 2, src: icono2, parrafo: 'Diseñamos un gestor de contraseñas para nuestro cliente utilizando nuestros conocimientos adquiridos en la TUP y nuestro curso Fullstack realizado previamente.' },
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias" :key="experencia.id">
                <img class="imagen-svg" :src="experencia.src" width="45rem" :alt="experencia.parrafo">
                <p>{{ experencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(39 97 43);
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: #fff;
}

.fecha {
    font-size: 1rem;
    color: #fff;
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>