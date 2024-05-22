<template>
  <div class="bottom-item">
    <p class="bottom-title">{{ title }}</p>
    <ul class="post-list">
      <li v-for="(post, index) in posts" :key="index" class="post-item">
        <span class="post-title">{{ post.title }}</span>
        <span class="post-author">
          <img src="@/assets/img/home/author_img.png" width="20px" alt="작성자">{{ post.author }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  posts: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.bottom-item {
  flex: 1;
  text-align: left; /* 텍스트 정렬을 왼쪽으로 변경 */
  margin: 0 10px;
  padding: 20px;
  border-radius: 10px;
  background-color: black; /* 배경색을 검정색으로 변경 */
  color: white; /* 글씨색을 흰색으로 변경 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.bottom-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  border-bottom: 1px solid #444; /* 하단 테두리 추가 */
  padding-bottom: 5px;
}

.post-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.post-item {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #444; /* 테두리 색상 변경 */
}

.post-title {
  font-weight: bold;
  flex: 1;
}

.post-author {
  color: #ccc; /* 글쓴이 색상 변경 */
  font-size: 14px;
  display: flex;
  align-items: center;
}

.icon {
  width: 16px;
  height: 16px;
  margin-right: 5px;
  background: url('/path/to/icon.png') no-repeat center center;
  background-size: contain;
}
</style>
