<template>
  <div>
    <NavBar />
    <!-- <RouterLink to="/">home</RouterLink> | 
    <RouterLink to="/mapview">은행지도</RouterLink> | 
    <RouterLink to="/communityview">커뮤니티</RouterLink> -->

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue';
</script>

<style scoped>

</style>
