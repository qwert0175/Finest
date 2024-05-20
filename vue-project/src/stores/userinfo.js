import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserInfoStore = defineStore('userinfo', () => {
    // 로그인 토큰
    const token = ref(null);
    const articles = ref([]);
    const username = ref(null);
    const API_URL = 'http://127.0.0.1:8000'

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


// // 새로고침 시 로그아웃되는 이슈 해결하려했으나 잘 안됨.
// import { ref } from 'vue'
// import { defineStore } from 'pinia'
// import axios from 'axios'

// export const useUserInfoStore = defineStore('userinfo', () => {
//   // 로그인 토큰
//   const token = ref(localStorage.getItem('authToken') || null)
//   const articles = ref([])
//   const username = ref(null)
//   const API_URL = 'http://127.0.0.1:8000'

//   const setToken = function(newToken) {
//     token.value = newToken
//     localStorage.setItem('authToken', newToken)
//     axios.defaults.headers.common['Authorization'] = `Token ${newToken}`
//   }

//   const clearToken = function() {
//     token.value = null
//     localStorage.removeItem('authToken')
//     delete axios.defaults.headers.common['Authorization']
//   }

//   const getArticles = function() {
//     axios({
//       method: 'get',
//       url: `${API_URL}/articles/`,
//       headers: {
//         Authorization: `Token ${token.value}`
//       }
//     })
//       .then(response => {
//         articles.value = response.data
//       })
//       .catch(error => {
//         console.log(error)
//       })
//   }

//   if (token.value) {
//     axios.defaults.headers.common['Authorization'] = `Token ${token.value}`
//   }

//   return { token, articles, username, API_URL, setToken, clearToken, getArticles }
// })
