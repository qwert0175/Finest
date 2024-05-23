<template>
  <div class="community-container">
    <div class="header">
      <h1 class="page-title">커뮤니티</h1>
      <RouterLink :to="{ name: 'CreateView' }" class="create-button">
        글쓰기
      </RouterLink>
    </div>
    <div class="search-bar">
      <select v-model="searchType" class="search-select">
        <option value="title">제목</option>
        <option value="author">작성자</option>
      </select>
      <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요" class="search-input" @keyup.enter="searchArticles">
      <button @click="searchArticles" class="search-button">검색</button>
    </div>
    <div v-if="loading" class="loading">로딩중...</div>
    <table v-else class="article-table">
      <thead>
        <tr>
          <th>분류</th>
          <th>제목</th>
          <th>작성자</th>
          <th>작성일</th>
          <th>좋아요</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in filteredArticles" :key="article.id">
          <td>{{ article.category }}</td>
          <td>
            <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }" class="article-link">
              {{ article.title }}
            </RouterLink>
          </td>
          <td>{{ article.user }}</td>
          <td>{{ formatDate(article.created_at) }}</td>
          <td>{{ article.likes }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { RouterLink } from 'vue-router'

const userInfoStore = useUserInfoStore()
const searchQuery = ref('')
const searchType = ref('title')
const articles = ref([])
const loading = ref(true)

const filteredArticles = computed(() => {
  if (!searchQuery.value) {
    return articles.value
  }
  return articles.value.filter(article => {
    if (searchType.value === 'title') {
      return article.title.includes(searchQuery.value)
    } else if (searchType.value === 'author') {
      return article.user.includes(searchQuery.value)
    }
  })
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

const fetchArticles = async () => {
  loading.value = true
  await userInfoStore.getArticles()
  articles.value = userInfoStore.articles.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
  loading.value = false
}

onMounted(async () => {
  await fetchArticles()
})

// Watch for changes in the userInfoStore's articles and update the local articles list
watch(() => userInfoStore.articles, (newArticles) => {
  articles.value = newArticles.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
})

</script>

<style scoped>
.community-container {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.page-title {
  font-size: 1.5em;
  color: #333;
}

.create-button {
  display: inline-block;
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  text-align: center;
  text-decoration: none;
}

.create-button:hover {
  background-color: #0056b3;
}

.search-bar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-select, .search-input, .search-button {
  padding: 10px;
  margin-right: 10px;
  font-size: 1em;
}

.search-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}

.loading {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
  color: #007bff;
}

.article-table {
  width: 100%;
  border-collapse: collapse;
}

.article-table th, .article-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

.article-table th {
  background-color: #f8f8f8;
}
</style>
