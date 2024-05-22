<template>
  <div>
    <h1>게시글 수정 페이지</h1>
    <form @submit.prevent="updateArticleInfo">
      <!-- <div>
        <label for="category">카테고리 : </label>
        <select v-model.trim="articleData.category" id="category">
          <option value="공지사항">공지사항</option>
          <option value="자유게시판">자유게시판</option>
        </select>
      </div> -->
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="articleData.title" id="title" >
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="articleData.content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserInfoStore } from '@/stores/userinfo'
import axios from 'axios'

const userInfoStore = useUserInfoStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

const articleData = ref({
  category: '',
  title: '',
  content: ''
})


onMounted(() => {
    axios ({
        method: 'get',
        url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        }
    })
    .then(res => {
      articleData.value = {
            category: res.data.category,
            title: res.data.title,
            content: res.data.content,
        }
    })
    .catch(err => {
        for (const e in err.response.data) {
            alert(`${e}: ${err.response.data[e]}`)
        }
    })
})

const updateArticleInfo = () => {
    axios({
        method: 'put',
        url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        },
        data: articleData.value
    })
    .then(res => {
        alert('게시글이 성공적으로 수정되었습니다.')
        router.push({ name: 'DetailView', params: { id: route.params.id } })
    })
    .catch(err => {
        for (const e in err.response.data) {
            alert(`${e}: ${err.response.data[e]}`)
        }
    })
}
</script>

<style scoped>
/* Add your styles here */
</style>
