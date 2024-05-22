<template>
    <div class="home row">
      <div class="top-container row">
        <div class="event-banner col-12 col-lg-8 p-0">
          <EventBanner />
        </div>
        <div class="exchange-calculator col-12 col-lg-4 p-0">
          <ExchangeCalculator />
        </div>
      </div>
      <div class="middle-container d-flex">
        <RouterLink class="nav-link" to="/product">
          <div class="middle-item product">
            <p>상품정보 조회</p>
          </div>
        </RouterLink>
        <RouterLink class="nav-link" to="/mapview">
          <div class="middle-item map">
            <p>주변은행 찾기</p>
          </div>
        </RouterLink>
        <RouterLink class="nav-link" to="/recommendview">
          <div class="middle-item recommend">
            <p>상품 추천 페이지</p>
          </div>
        </RouterLink>
      </div>
      <div class="bottom-container d-flex">
        <NoticeBoard title="공지사항" :posts="noticePosts" />
        <NoticeBoard title="자유게시판" :posts="boardPosts" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import EventBanner from '@/components/EventBanner.vue';
  import ExchangeCalculator from '@/components/ExchangeCalculator.vue';
  import NoticeBoard from '@/components/NoticeBoard.vue';
  
  const noticePosts = ref([]);
  const boardPosts = ref([]);
  const loading = ref(false);
  const error = ref(null);
  
  const fetchPosts = async () => {
    loading.value = true;
    try {
      const response = await axios.get('http://127.0.0.1:8000/articles/homeview/');
      noticePosts.value = response.data.notice;
      boardPosts.value = response.data.board;
    } catch (err) {
      error.value = '정보를 불러오는데 실패했습니다. 다시 시도해주세요';
    } finally {
      loading.value = false;
    }
  };
  
  onMounted(fetchPosts);
  </script>
  
  <style scoped>
  .row {
    --bs-gutter-x: 0;
  }
  
  .top-container {
    margin-bottom: 20px;
  }
  
  .middle-container {
    display: flex;
    justify-content: space-around;
    margin: 30px 0;
  }
  
  .middle-item {
    color: white;
    text-align: center;
    width: 250px;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 20px;
  }
  
  .product {
    background-color: #3751FE;
  }
  
  .map {
    background-color: #E47643;
  }
  
  .recommend {
    background-color: black;
  }
  
  .bottom-container {
    display: flex;
    justify-content: space-around;
    width: 100%;
    padding: 20px;
    background-color: #f8f9fa;
  }
  
  @media (max-width: 768px) {
    .middle-container {
      flex-direction: column;
      align-items: center;
    }
  
    .middle-item {
      margin-bottom: 20px;
    }
  
    .bottom-container {
      flex-direction: column;
      align-items: center;
    }
  
    .bottom-item {
      margin-bottom: 20px;
      width: 80%;
    }
  }
  </style>
  