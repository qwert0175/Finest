<template>
  <div>
    <h1>게시글 상세 페이지</h1>
    <div v-if="article">
      <p>글 번호 : {{ article.id }}</p>
      <p>작성자 : {{ article.user }}</p>
      <p>분류 : {{ article.category }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>게시일 : {{ formatDate(article.created_at) }}</p>
      <p>수정일 : {{ formatDate(article.updated_at) }}</p>

      <button @click="editArticle">수정</button>
      <button @click="deleteArticle">삭제</button>
    </div>

    <div v-if="article">
      <h2>댓글</h2>
      <form @submit.prevent="createComment">
        <div>
          <label for="commentContent">댓글 내용:</label>
          <textarea id="commentContent" v-model="newComment.content" required></textarea>
        </div>
        <button type="submit">댓글 작성</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { useRoute, useRouter } from 'vue-router'

const userInfoStore = useUserInfoStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const newComment = ref({
  content: ''
})


// 게시일, 수정일 맞춤 양식으로 변환
const formatDate = (dateString) => {
  const date = new Date(dateString)
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')
  const hours = String(date.getHours()).padStart(2, '0')
  const minutes = String(date.getMinutes()).padStart(2, '0')
  return `${year}.${month}.${day} ${hours}:${minutes}`
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userInfoStore.token}`
    }
  })
    .then((response) => {
      // console.log(response.data)
      article.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})

const deleteArticle = () => {
  if (confirm('정말로 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
      .then(() => {
        alert('삭제되었습니다.')
        router.push({ name: 'communityview' }).then(() => {
          location.reload()
        })
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

const editArticle = () => {
  router.push({ name: 'UpdateView', params: { id: article.value.id } })
}

const createComment = () => {
  axios({
    method: 'post',
    url: `${userInfoStore.API_URL}/articles/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${userInfoStore.token}`
    },
    data: {
      content: newComment.value.content
    }
  })
    .then(() => {
      alert('댓글이 작성되었습니다.')
      newComment.value.content = '' // Clear the comment input field
      // Reload the page or update the comment list if implemented
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>


<style>

</style>
