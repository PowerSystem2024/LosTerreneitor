<script setup>
import NavBar from "./components/NavBar.vue";
import DatosPersonales from "./components/DatosPersonales.vue";
import ComponentEducation from "./components/ComponentEducation.vue";
import ComponentExperience from "./components/ComponentExperience.vue";
import ComponentProjects from "./components/ComponentProjects.vue";
import ComponentHabilidades from "./components/ComponentHabilidades.vue";
import ComponentIntereses from "./components/ComponentIntereses.vue";
</script>

<template>
  <header>
    <NavBar />
    <DatosPersonales />
  </header>
  <main>
    <section id="educacion">
      <h2>Educación - Cursos</h2>
      <ComponentEducation />
    </section>

    <section id="experiencia">
      <h2>Experiencia</h2>
      <ComponentExperience />
    </section>

    <section id="proyectos">
      <h2>Proyectos</h2>
      <ComponentProjects />
    </section>

    <section id="habilidades">
      <h2>Habilidades</h2>
      <ComponentHabilidades />
    </section>

    <section id="intereses">
      <h2>Intereses</h2>
      <ComponentIntereses />
    </section>
  </main>
  <footer>
    <a href="#top">
      <button class="botonInicio">Inicio</button>
    </a>
    <p>© Los Terreneitor - Portafolio Web - UTN FRSR 2024</p>
  </footer>
</template>

<style scoped></style>
