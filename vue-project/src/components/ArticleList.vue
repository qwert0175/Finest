<template>
  <div>
    <h3>Article List</h3>
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
