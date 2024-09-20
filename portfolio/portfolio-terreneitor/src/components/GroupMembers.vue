<script setup lang="js">
import { ref } from 'vue'

const groupMembers = ref([])

const members = [
  {
    name: 'Agustín',
    avatar: 'https://avatars.githubusercontent.com/u/166578771?v=4',
    url: 'https://github.com/agus-salinas'
  },
  {
    name: 'Franco',
    avatar: 'https://avatars.githubusercontent.com/u/134340520?v=4',
    url: 'https://github.com/Mendoxeneixe'
  },
  {
    name: 'Elias',
    avatar: 'https://avatars.githubusercontent.com/u/164105708?v=4',
    url: 'https://github.com/eliasdjacob'
  },
  {
    name: 'Juan Pablo',
    avatar: 'https://avatars.githubusercontent.com/u/166343183?v=4',
    url: 'https://github.com/jpbatallon'
  },
  {
    name: 'Maximiliano',
    avatar: 'https://avatars.githubusercontent.com/u/106635349?v=4',
    url: 'https://github.com/maxidtomio'
  },
  {
    name: 'Gabriel',
    avatar: 'https://avatars.githubusercontent.com/u/93176365?v=4',
    url: 'https://github.com/solidsnk86'
  }
]
groupMembers.value = members
</script>

<template>
  <section class="grid">
    <div v-for="(member, index) in groupMembers" :key="index">
      <a :href="member.url" class="avatar-container">
        <img :src="member.avatar" :alt="member.name" />
        <small>{{ member.name }}</small>
      </a>
    </div>
  </section>
</template>

<style lang="css" scoped>
section {
  display: flex;
  width: 100%;
  padding: 10px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 16px;
}

.avatar-container {
  text-decoration: none;
  color: var(--color-text);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

img {
  width: 65px;
  height: 65px;
  border-radius: 50%;
}

img:hover {
  animation: 1.3s infinite alternate zoomin;
}

@keyframes zoomin {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.2);
  }
}

small {
  font-weight: 600;
  text-align: center;
}
</style>
