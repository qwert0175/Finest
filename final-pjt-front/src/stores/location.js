import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useLocationStore = defineStore('location', () => {
  // 위경도 변수
  const latitude = ref(37.5642135);
  const longitude = ref(127.0016985);
  
  // 현재 위치 가져오기
  navigator.geolocation.getCurrentPosition((position) => {
    latitude.value = position.coords.latitude;
    longitude.value = position.coords.longitude;
  });

  return { latitude, longitude }
})
