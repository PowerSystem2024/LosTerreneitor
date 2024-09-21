<script setup lang="ts">
import { Construction } from 'lucide-vue-next'
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="card-container">
    <Construction class="construction-icon" />
    <h1 class="msg">{{ msg }}</h1>
  </div>
</template>

<style lang="css" scoped>
.card-container {
  display: flex;
  padding: 16px;
  margin: 50px auto;
  align-items: center;
  border: 1px solid var(--color-border);
  border-radius: 10px;
  gap: 8px;
  background: linear-gradient(333deg, var(--purple), var(--green));
  background-size: 180% 180%;
  animation: gradient-animation 6s ease infinite;
}

@keyframes gradient-animation {
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

.construction-icon {
  color: #121212;
  width: 24px;
  height: 24px;
}

.msg {
  font-size: 1.5rem;
  font-weight: 800;
  color: #121212;
}
</style>
