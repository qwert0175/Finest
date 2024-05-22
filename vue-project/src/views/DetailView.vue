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
          <div class="author-details">
            <router-link :to="{ name: 'profile', params: { username: article.user } }" class="username">{{ article.user }}</router-link>
            <p class="rank">매니저</p>
          </div>
        </div>
      </div>

      <div class="article-date">
        <p>게시일 : {{ formatDate(article.created_at) }}</p>
        <p>수정일 : {{ formatDate(article.updated_at) }}</p>
      </div>
    </div>

    <div class="article-content">
      <p>{{ article.content }}</p>
      <div class="article-content-bottom">
        <div class="comment-image-like-count-wrapper">
          <div class="comment-image">
            <p>❤</p>
          </div>
          <p class="comment-count">좋아요 {{ comments.length }}개</p>
          <div class="comment-image">
            <img src="/src/assets/img/comment_image.jpg" alt="comment-image">
          </div>
          <p class="comment-count">댓글 {{ comments.length }}개</p>
        </div>
        <div class="share-image-text-wrapper">
          <div class="share-image" @click="share">
            <img src="/src/assets/img/share_image.jpg" alt="share-image">
          </div>
          <p class="share-text" @click="share">공유 |</p>
          <p class="report" @click="reportArticle">신고</p>
        </div>
      </div>
    </div>

    <div class="article-bottom">
      <form @submit.prevent="addComment" class="comment-create-actions">
        <div class="comment-create-input">
          <input type="text" v-model="newComment" placeholder="댓글을 입력하세요" />
        </div>
        <div class="comment-create-button">
          <button type="submit">댓글 등록</button>
        </div>
      </form>
      <ul class="comments-list">
        <li v-for="comment in comments" :key="comment.id" class="comment-list">
          <p class="comment">{{ comment.user }} : {{ comment.content }}</p>
          <div class="comment-date-delete-wrapper">
            <p class="comment-date">{{ formatDate(comment.created_at) }}</p>
            <!-- <p>{{ currentUser }}</p> -->
            <div v-if="isCommentAuthor(comment.user)" class="comment-delete-button">
              <button @click="deleteComments(comment.id)">삭제</button>
            </div>
          </div>
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
import { useRoute, useRouter } from 'vue-router'
import { useUserInfoStore } from '@/stores/userinfo'
import { useModalStore } from '@/stores/modal'

const userInfoStore = useUserInfoStore()
// console.log(userInfoStore.token)
const modalStore = useModalStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref([])
const newComment = ref('')
const commentId = ref('')
const currentUser = userInfoStore.username

const goCommunity = function () {
  router.push({ name: 'communityview' })
}

const reportArticle = () => {
  modalStore.showModal('신고되었습니다🤬')
}

const share = () => {
  modalStore.showModal('주소가 복사되었습니다😁')
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
  if (confirm('정말로 게시글을 삭제하시겠습니까❗❓')) {
    axios({
      method: 'delete',
      url: `${userInfoStore.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${userInfoStore.token}`
      }
    })
    .then(() => {
      modalStore.showModal('삭제되었습니다.')
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
  if (confirm('정말로 댓글을 삭제하시겠습니까❗❓')) {
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
      modalStore.showModal('댓글이 삭제되었습니다.')
    } catch (error) {
      console.error('Failed to delete comment:', error)
      modalStore.showModal('댓글 삭제에 실패했습니다.')
    }
  }
}

const isCommentAuthor = (commentUser) => {
  return commentUser.toLowerCase() === currentUser
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
  margin: 50px auto;
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
    margin-top: 20px;
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
.author-details {
  display: flex;
  align-items: center;
}
.username {
    font-size: 0.9em; 
}
.rank {
  color: #999;
  font-size: 0.9em;
  margin: 0px;
  margin-left: 5px;
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
.article-content-bottom {
  display: flex;
  justify-content: space-between;
  margin-top: 100px;
}
.comment-image-like-count-wrapper {
  display: flex;
  justify-content: start;
}
.comment-image {
  margin-right: 10px;
  margin-left: 10px;
}
.share-image-text-wrapper {
  display: flex;
  justify-content: start;  
}
.share-image {
  margin-right: 10px;
  cursor: pointer;
}
.share-text {
  cursor: pointer;
}
.share-text:hover {
  text-decoration: underline;
}
.report {
  margin-left: 10px;
  color: red;
  font-weight: bolder;
  cursor: pointer;
}
.report:hover {
  text-decoration: underline;
}

.article-bottom {
  border-bottom: 1px solid #ddd;
  margin: 10px 0;
}

.comment-create-actions {
  /* display: flex;
  flex-direction: column; */
  display: flex;
  justify-content: start;
  align-items: center; 
  margin-top: 20px;
  margin-bottom: 10px;
}
.comment-create-input {
  flex: 1;
  margin-left: 10px;
  margin-right: 20px;
}
.comment-create-input input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.comment-create-button button {
  background-color: #007bff;
  color: white;
  padding: 10px 10px;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  font-size: 0.9em;
}
.comment-create-button button:hover {
  background-color: #0056b3;
}

.comments-list {
  list-style-type: none;
  padding: 10px;
}
.comment-list {
  padding: 10px 0;
  display: flex;
  flex-direction: column;
  align-items: start;
}
.comment {
  font-size: 1em;
  margin: 0;
}
.comment-date-delete-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 5px;
}
.comment-date {
  font-size: 0.9em;
  color: #999;
  margin: 5px 0
}
.comment-delete-button {
  margin-left: 10px;
}
.comment-delete-button button {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 15px;
  cursor: pointer;
  font-size: 0.7em;
}
.comment-delete-button button:hover {
  background-color: #c82333;
}

.back-button {
  display: block;
  margin-top: 20px;
  border-radius: 4px;
  text-align: center;
  border: none;
  cursor: pointer;
  font-size: 1em;
}



</style>
