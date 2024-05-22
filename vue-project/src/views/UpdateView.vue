<template>
  <div class="update-container">
    <h1 class="page-title">게시글 수정 페이지</h1>
    <form @submit.prevent="updateArticleInfo" class="update-form">
      <div class="form-group">
        <label for="title" class="form-label">제목 : </label>
        <input type="text" v-model.trim="articleData.title" id="title" class="form-input">
      </div>
      <div class="form-group">
        <label for="content" class="form-label">내용 : </label>
        <textarea v-model.trim="articleData.content" id="content" class="form-textarea"></textarea>
      </div>
      <div class="form-actions">
        <input type="submit" class="submit-button" value="저장">
        <button type="button" class="cancel-button" @click="cancelUpdate">취소</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserInfoStore } from '@/stores/userinfo'
import { useModalStore } from '@/stores/modal'
import axios from 'axios'

const userInfoStore = useUserInfoStore()
const modalStore = useModalStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

const articleData = ref({
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
          modalStore.showModal(`${e}: ${err.response.data[e]}`)
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
      modalStore.showModal('게시글이 수정되었습니다😊')
        router.push({ name: 'DetailView', params: { id: route.params.id } })
    })
    .catch(err => {
        for (const e in err.response.data) {
          modalStore.showModal(`${e}: ${err.response.data[e]}`)
        }
    })
}

const cancelUpdate = () => {
  router.go(-1)
}
</script>

<style scoped>
.update-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 50px auto;
}

.page-title {
  margin-bottom: 20px;
  font-size: 1.5em;
  color: #333;
}

.update-form {
  width: 100%;
}

.form-group {
  margin-bottom: 15px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

.form-input, .form-textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1em;
}

.form-textarea {
  min-height: 200px;
  resize: vertical;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.submit-button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
}

.submit-button:hover {
  background-color: #0056b3;
}

.cancel-button {
  background-color: #dc3545;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
}

.cancel-button:hover {
  background-color: #c82333;
}

</style>
