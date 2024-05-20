import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
// import { useRouter } from 'vue-router'

export const useUserInfoStore = defineStore('userinfo', () => {
    // 로그인 토큰
    const token = ref(null);
    const articles = ref([]);
    const username = ref(null);
    const API_URL = 'http://127.0.0.1:8000'

    // const router = useRouter()

    const getArticles = function () {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then(response => {
          articles.value = response.data
        })
        .catch(error => {
          console.log(error)
        })
    };
  
    return { token, articles, username, API_URL, getArticles };
  })
  