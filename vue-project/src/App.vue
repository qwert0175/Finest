<template>
  <div>
    <NavBar />
    <RouterView />
    <Modal />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue';
import Modal from '@/components/Modal.vue'
</script>

<style scoped>

</style>
