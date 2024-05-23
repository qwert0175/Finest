<template>
  <div>
    <h3>공지사항 & 자유게시판</h3>
    <hr>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useUserInfoStore } from '@/stores/userinfo'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useUserInfoStore()
</script>
