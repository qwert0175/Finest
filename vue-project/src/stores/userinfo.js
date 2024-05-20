import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserInfoStore = defineStore('userinfo', () => {
    // 로그인 토큰
    const token = ref(null);
  
    return { authToken }
  })
  