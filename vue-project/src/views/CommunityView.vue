<template>
    <div>
        <h1>커뮤니티</h1>
        <RouterLink :to="{ name: 'CreateView' }">
            [CREATE]
            <hr>
        </RouterLink>
        <ArticleList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const userInfoStore = useUserInfoStore();

onMounted(() => {
    userInfoStore.getArticles()
})
</script>

<style scoped>

</style>