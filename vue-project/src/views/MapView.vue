<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">은행지도</p>
    </div>
    <div class="map-container">
      <div>
        <div>
          <button class="map-option" :class="{ onSelectMode: mapMode === 1 }" @click="changeMapMode(1)">주변 은행</button>
          <button class="map-option" :class="{ onSelectMode: mapMode === 2 }" @click="changeMapMode(2)">위치 검색</button>
        </div>
        <KakaoMap v-if="mapMode === 1"/>
        <SearchMap v-else-if="mapMode === 2"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import KakaoMap from '@/components/KakaoMap.vue';
import SearchMap from '@/components/SearchMap.vue';
const mapMode = ref(1)
const changeMapMode = (mode) => {
  mapMode.value = mode
}
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

.map-option {
  color: white;
  background-color: #E47643;
  border: 1px solid black;
  border-radius: 7px 7px 0px 0px;
  padding: 10px;
}

.onSelectMode {
  background-color: #008000;
}
</style>