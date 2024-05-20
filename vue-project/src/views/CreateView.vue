<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="category">카테고리 : </label>
        <input type="text" v-model.trim="category" id="category">
      </div>
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { useRouter } from 'vue-router'

const store = useUserInfoStore()
const category = ref(null)
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/`,
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
      // console.log(response.data)
      router.push({ name: 'communityview' })
    })
    .catch((error) => {
      console.log(error)
    })
}

</script>

<style>

</style>
