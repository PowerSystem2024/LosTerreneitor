<script setup>

import { ref } from 'vue';
import FondoIntereses from './FondoIntereses.vue';
const intereses = ref([
    'Perfeccionamiento de nuestras skills: A través del aprendizaje constante buscamos ser mejores profesionales y crecer en el rubro.',
    'Trabajo en equipo: Tenemos como regla que siempre prime el trabajo en equipo y la buena predisposición de todos los integrantes para que sea un clima ameno de trabajo.',
    'Nuevos conocimientos: Estamos en continua búsqueda de nuevos conocimientos para satisfacer todas las necesidades de nuestros clientes de la mejor manera posible.',
    'Descanso grupal: Creemos que compartir momentos como equipo fuera del entorno laboral fomenta las buenas relaciones y mejora la comunicación entre todos los integrantes del grupo.'
]);

</script>


<template>

 <div class="intereses-contenedor">
        <FondoIntereses />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>

</template>

<style scoped>

.intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 1rem;
    z-index: 1;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
    z-index: 1;
}

.item {
    margin-bottom: 1rem;
}

</style>