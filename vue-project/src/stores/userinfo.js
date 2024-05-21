import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserInfoStore = defineStore('userinfo', () => {
    // 로그인 토큰
    const token = ref(sessionStorage.getItem('token'));
    const articles = ref([]);
    const username = ref(null);
    const API_URL = 'http://127.0.0.1:8000'
    const isDeposit = ref(true);
    const commentList = ref([]);

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
    
    const newComment = function (id, content) {
      console.log(token.value)
      return axios({
        method: 'POST',
        url: `${API_URL}/articles/${id}/comments/`, // URL 형식 확인
        headers: {
          // Authorization: sessionStorage.getItem('token'),
          Authorization: `Token ${token.value}`
        },
        data: {
          "content": content
        },
      })
      .then(function (response) {
        console.log('Comment created:', response.data)
        return response.data;
      })
      .catch(function (error) {
        console.log(error)
        throw error;
      })
    }
  
    const viewComment = async function (id) {
      try {
        const response = await axios({
          method: 'GET',
          url: `${API_URL}/articles/${id}/comments/`,
          headers: { 
            Authorization: `Token ${token.value}` 
          }
        });
        commentList.value = response.data;
        console.log(commentList.value);
      } catch (err) {
        console.error('Failed to fetch articles:', err);
      }
    };
  
    const deleteComment = function (id, commentId) {  
      axios({
        method: 'DELETE',
        url: `${API_URL}/articles/${id}/comment_detail/${commentId}/`,
        headers: {
          Authorization: sessionStorage.getItem('token'),
        },
      })
      .then(function(response) {
        console.log('Comment deleted:', response.data)
      })
      .catch(function(error) {
        console.log(error)
      })      
    }

    return { token, articles, username, API_URL, getArticles, isDeposit, newComment, viewComment, deleteComment };
  })


