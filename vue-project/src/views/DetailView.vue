<template>
  <div>
    <h1>DetailView</h1>
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
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { useRoute, useRouter } from 'vue-router'

const store = useUserInfoStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const editMode = ref(false)
const updatedArticle = ref({
  category: '',
  title: '',
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
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
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

const updateArticle = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      category: updatedArticle.value.category,
      title: updatedArticle.value.title,
      content: updatedArticle.value.content
    }
  })
    .then((response) => {
      article.value = response.data
      editMode.value = false
      alert('수정되었습니다.')
    })
    .catch((error) => {
      console.log(error)
    })
}

const deleteArticle = () => {
  if (confirm('정말로 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
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
  router.push({ name: 'updateview', params: { id: article.id } })
}

</script>

<style>

</style>
