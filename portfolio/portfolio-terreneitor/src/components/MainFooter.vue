<template>
  <footer>
    <!-- Se obtiene el año actual con new Date().getFullYear() -->
    <small>&copy;Terreneitor UTN-FRSR {{ new Date().getFullYear() }}</small>
  </footer>
</template>

<style lang="css" scoped>
footer {
  display: flex;
  width: 100%;
  border-top: 1px solid var(--color-border);
  justify-content: center;
  padding-top: 60px;
  z-index: 99;
}
small {
  font-weight: 700;
}
</style>
