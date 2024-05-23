<template>
  <div class="create-container">
    <h1 class="page-title">게시글 작성</h1>
    <form @submit.prevent="createArticle" class="create-form">
      <div class="form-group">
        <label for="category" class="form-label">카테고리 : </label>
        <select v-model="category" id="category" class="form-input">
          <option value="공지사항">공지사항</option>
          <option value="자유게시판">자유게시판</option>
        </select>
      </div>
      <div class="form-group">
        <label for="title" class="form-label">제목 : </label>
        <input type="text" v-model.trim="title" id="title" class="form-input">
      </div>
      <div class="form-group">
        <label for="content" class="form-label">내용 : </label>
        <textarea v-model.trim="content" id="content" class="form-textarea"></textarea>
      </div>
      <div class="form-actions">
        <input type="submit" value="저장" class="submit-button">
        <button type="button" class="cancel-button" @click="cancelCreate">취소</button>
      </div>
    </form>
  </div>
</template>


<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { useRouter } from 'vue-router'

const store = useUserInfoStore()
const category = ref(null)
const title = ref(null)
const content = ref(null)
const router = useRouter()

onMounted(() => {
  if (store.token === null) {
    router.push({ name: 'loginview' })
    return
  }
})

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/create/`,
    data: {
      category: category.value,
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      router.push({ name: 'communityview' })
    })
    .catch((error) => {
      console.log(error)
    })
}

const cancelCreate = () => {
  router.go(-1)
}

</script>

<style>
.create-container {
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

.create-form {
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
