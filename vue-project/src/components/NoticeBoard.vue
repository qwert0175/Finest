<template>
    <div class="bottom-item">
      <p class="bottom-title">{{ title }}</p>
      <ul class="post-list">
        <li v-for="(post, index) in posts" :key="index" class="post-item">
          <span class="post-title">{{ post.title }}</span>
          <span class="post-author">{{ post.author }}</span>
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
    text-align: center;
    margin: 0 10px;
    padding: 20px;
    border-radius: 10px;
    background-color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .bottom-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
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
    border-bottom: 1px solid #ddd;
  }
  
  .post-title {
    font-weight: bold;
  }
  
  .post-author {
    color: #999;
    font-size: 14px;
  }
  </style>
  