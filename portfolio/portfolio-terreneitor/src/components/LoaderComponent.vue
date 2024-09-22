<template>
  <div class="loader"></div>
</template>

<style lang="css" scoped>
.loader {
  width: 45px;
  height: 45px;
  border-top: 6px solid var(--green-light);
  border-left: 6px solid rgba(104, 104, 104, 0.5);
  border-bottom: 6px solid rgba(104, 104, 104, 0.5);
  border-right: 6px solid rgba(104, 104, 104, 0.5);
  border-radius: 50%;
  animation: 2s linear infinite spinner;
}

@keyframes spinner {
  to {
    transform: rotate(360deg);
  }
}
</style>
