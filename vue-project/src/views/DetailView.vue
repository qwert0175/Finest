<template>
  <div v-if="article" class="article">
    <div class="article-heder">
      <div class="category">
        <img src="/src/assets/img/category.jpg" alt="category Icon" class="category-icon">
        <span class="category-text">{{ article.category }}</span>
      </div>
      
      <div class="article-heder-actions">
        <button @click="editArticle">수정</button> |
        <button @click="deleteArticle">삭제</button>
      </div>
    </div>
    <p class="title">{{ article.title }}</p>

    <div class="article-heder-bottom">
      <div class="article-author">
        <div class="author-info">
          <div class="author-avatar">
            <img src="/src/assets/img/author_image.jpg" alt="author-image">
          </div>
          <p class="username">{{ article.user }}</p>
          <p class="rank">매니저</p>
        </div>
      </div>

      <div class="article-date">
        <p>게시일 : {{ formatDate(article.created_at) }}</p>
        <p>수정일 : {{ formatDate(article.updated_at) }}</p>
      </div>
    </div>

    <div class="article-content">
      <p>{{ article.content }}</p>
    </div>

    <div class="comments">
      <h3>댓글</h3>
      <form @submit.prevent="addComment">
        <input type="text" v-model="newComment" placeholder="댓글을 입력하세요" />
        <div class="click-button">
          <button type="submit">등록</button>
        </div>
      </form>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p>{{ comment.user }} : {{ comment.content }}</p>
          <p>{{ formatDate(comment.created_at) }}</p>
          <button @click="deleteComments(comment.id)">삭제</button>
        </li>
      </ul>
    </div>

    <div class="back-button">
    <button @click="goCommunity">목록</button> 
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo'
import { useRoute, useRouter } from 'vue-router'

const userInfoStore = useUserInfoStore()
console.log(userInfoStore.token)
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref([])
const newComment = ref('')
const commentId = ref('')

const goCommunity = function () {
  router.push({ name: 'communityview' })
}

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


const deleteArticle = () => {
  if (confirm('정말로 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
    .then(() => {
        alert('삭제되었습니다.')
        router.push({ name: 'communityview' })
    })
  }
}
  
const editArticle = () => {
  router.push({ name: 'UpdateView', params: { id: article.value.id } })
}

const addComment = async () => {
  try {
    // 새 댓글 등록
    const newCommentResponse = await userInfoStore.newComment(route.params.id, newComment.value)
    console.log('New comment added:', newCommentResponse)

    // 댓글 등록 후 댓글 목록 다시 가져오기
    const response = await axios({
      method: 'get',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/comments/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
    comments.value = response.data
    console.log('Comments:', comments.value)

    // 입력 필드 초기화
    newComment.value = '' 
  } catch (error) {
    console.error('Failed to add comment:', error)
    alert('댓글 등록에 실패했습니다.')
  }
}

const deleteComments = async (commentId) => {
  try {
    await axios({
      method: 'delete',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/comment_detail/${commentId}/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
    // 댓글 삭제 후 댓글 목록 다시 가져오기
    const response = await axios({
      method: 'get',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/comments/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
    comments.value = response.data
  } catch (error) {
    console.error('Failed to delete comment:', error)
    alert('댓글 삭제에 실패했습니다.')
  }
}
  
onMounted(() => {
  console.log(userInfoStore.token)
  axios({
    method: 'get',
    url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${userInfoStore.token}`
    }
  })
    .then((response) => {
      // console.log(response.data)
      article.value = response.data
      // 댓글 정보 가져오기
      return axios({
        method: 'get',
        url: `${userInfoStore.API_URL}/articles/${route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${userInfoStore.token}`
        }
      })
    })
    .then((response) => {
      // 댓글 정보 설정
      comments.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>


<style>
.article {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 10px;
  background-color: #fff;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}


.article-heder {
    display: flex;
    justify-content: space-between;
    align-items: center; 
}

.article-heder-actions {
    display: flex;
    gap: 10px; 
}
.article-heder-actions button {
  background: none;
  border: none;
  color: #999;
  font-size: 0.9em;
  cursor: pointer;
  padding: 0;
}
.title {
    font-size: 1.5em; 
    font-weight: bold;
}

.article-heder-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center; /* Align items vertically */
}

.author-info {
    display: flex;
    align-items: center; /* Ensure the avatar and username are vertically aligned */
}
.author-avatar {
    margin-right: 10px; /* Space between the avatar and username */
}
.author-avatar img {
    width: 40px; 
    height: 40px; 
    border-radius: 50%; 
}
.username {
    font-size: 0.9em; 
    /* font-weight: bold;  */
}
.rank {
  color: #999;
  font-size: 0.9em;
  margin-left: 10px;
}

.article-date {
  text-align: right;
  color: #999;
  font-size: 0.9em;
  margin-top: 10px;
}
.article-date p {
  margin: 0;
  line-height: 1.5;
}

.article-content {
  padding: 10px;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  margin: 10px 0;
}

</style>
