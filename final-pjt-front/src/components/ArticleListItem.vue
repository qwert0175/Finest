<template>
  <div>
    <h5>글 번호 : {{ article.id }}</h5>
    <p>분류 : {{ article.category }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <RouterLink 
      :to="{ name: 'DetailView', params: { id: article.id }}"
    >
      [DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})

</script>
