<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">은행지도</p>
    </div>
    <div class="map-container">
      <KakaoMap />
    </div>
  </div>
</template>

<script setup>
import KakaoMap from '@/components/KakaoMap.vue';
</script>
  
<style scoped>
.page-title {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #E47643;
  height: 50px;
  font-size: 20px;
  color: white;
}

.page-title-text {
  margin: 0;
}

.map-container {
  display: flex;
  justify-content: center;
  padding: 50px;
}
</style>