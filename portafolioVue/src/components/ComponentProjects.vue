<script setup>
import proyecto1 from "/src/assets/obraConstruccion.jpg";
import proyecto2 from "/src/assets/obraConstruccion.jpg";
import proyecto3 from "/src/assets/obraConstruccion.jpg";
import { ref } from "vue";

var misProyectos = ref([]);
misProyectos.value = [
  {
    id: 1,
    src: proyecto1,
    titulo: "Proyecto en construcción",
    descripcion:
      "Proyecto en construcción del equipo Los Terreneitor, grupo de 4 integrantes de la UTN FRSR",
    projectoLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto",
  },
  {
    id: 2,
    src: proyecto2,
    titulo: "Proyecto en construcción",
    descripcion:
      "Proyecto en construcción del equipo Los Terreneitor, grupo de 4 integrantes de la UTN FRSR",
    projectoLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto",
  },
  {
    id: 3,
    src: proyecto3,
    titulo: "Proyecto en construcción",
    descripcion:
      "Proyecto en construcción del equipo Los Terreneitor, grupo de 4 integrantes de la UTN FRSR",
    projectoLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto",
  },
];
</script>

<template>
  <div class="galeria">
    <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
      <img :src="proyecto.src" :alt="proyecto.titlulo" />
      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{ proyecto.descripcion }}</p>
        <div class="proyecto-links">
          <a
            :href="proyecto.projectoLink"
            class="btn-ver-mas"
            target="_blank"
            rel="noopener noreferrer"
            >Ver Proyecto</a
          >
          <a
            :href="proyecto.githubLink"
            class="github-link"
            target="_blank"
            rel="noopener noreferrer"
            >Ver Código en GitHub</a
          >
        </div>
      </div>
    </li>
  </div>
</template>

<style scoped>
.galeria {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
  justify-content: center;
  background: linear-gradient(-45deg, #27612b, #358d3b, #54c45c);
  background-size: 400% 400%;
  animation: gradient 10s ease infinite;
  border-radius: 10px;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.proyecto {
  display: flex;
  flex-direction: column;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background-color: #f9f9f9;
  max-width: 222px;
  flex: 1 1 300px;
}

.proyecto img {
  width: 100%;
  height: auto;
  display: block;
}

.proyecto-info {
  padding: 15px;
  text-align: center;
}

.proyecto-info h3 {
  margin: 10px 0;
  font-size: 1.3em;
  color: #333;
}

.proyecto-info p {
  margin: 10px 0;
  font-size: 1em;
  color: #666;
}

.proyecto-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 30px;
}

.proyecto-links .btn-ver-mas {
  background-color: rgba(0, 189, 126, 0.544);
  color: #fff;
  padding: 10px 15px;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s;
  margin-top: 1rem;
}

.proyecto-links .btn-ver-mas:hover {
  background-color: hsl(159, 94%, 25%);
}

.proyecto-links .github-link {
  color: #333;
  text-decoration: none;
  font-size: 0.9em;
}

.proyecto-links .github-link:hover {
  text-decoration: underline;
}
</style>
