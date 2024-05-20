<template>
  <div>
    <h1>Edit Post</h1>
    <form @submit.prevent="updatePost">
      <div>
        <label for="category">Category:</label>
        <input type="text" v-model="form.category" id="category" placeholder="Enter category" />
      </div>
      <div>
        <label for="title">Title:</label>
        <input type="text" v-model="form.title" id="title" placeholder="Enter title" />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea v-model="form.content" id="content" placeholder="Enter content"></textarea>
      </div>
      <button type="submit">Save</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserInfoStore } from '@/stores/userinfo'
import axios from 'axios'

const store = useUserInfoStore()
const route = useRoute()
const router = useRouter()

const form = ref({
  category: '',
  title: '',
  content: ''
})

const fetchPost = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      const post = response.data
      form.value.category = post.category
      form.value.title = post.title
      form.value.content = post.content
    })
    .catch((error) => {
      console.log(error)
    })
}

const updatePost = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      category: form.value.category,
      title: form.value.title,
      content: form.value.content
    }
  })
    .then(() => {
      alert('Post updated successfully')
      router.push({ name: 'detailview', params: { id: route.params.id } })
    })
    .catch((error) => {
      console.log(error)
    })
}

onMounted(() => {
  fetchPost()
})
</script>

<style scoped>
/* Add your styles here */
</style>
