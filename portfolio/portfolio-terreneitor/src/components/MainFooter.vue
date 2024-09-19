<template>
  <footer>
    <small>&copy;Terreneitor {{ new Date().getFullYear() }}</small>
  </footer>
</template>

<style lang="css" scoped>
footer {
  bottom: 12px;
  display: flex;
  width: 100%;
  border-top: 1px solid var(--color-border);
  justify-content: center;
  padding-top: 33px;
}
</style>
