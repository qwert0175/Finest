<template>
  <div class="home-container">
    <div class="home">
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
          <img src="@/assets/img/home/home_img_1.png" alt="">
          <span> 예적금 페이지</span>
          <div class="middle-item product"></div>
        </RouterLink>
        <RouterLink class="nav-link" to="/mapview">
          <img src="@/assets/img/home/home_img_2.png" alt="">
          <span> 내 주변 은행은 어디?</span>
          <div class="middle-item map"></div>
        </RouterLink>
        <RouterLink class="nav-link" to="/recommendview">
          <img src="@/assets/img/home/home_img_3.png" alt="">
          <span>나한테 딱 맞는 상품추천</span>
          <div class="middle-item recommend"></div>
        </RouterLink>
      </div>
      <div class="bottom-container d-flex">
        <NoticeBoard title="공지사항" :posts="noticePosts" />
        <NoticeBoard title="자유게시판" :posts="boardPosts" />
      </div>
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
.home-container {
  width: 100%;
  background-color: black;
  display: flex;
  justify-content: center;
}

.home {
  max-width: 1200px; /* 홈 뷰의 최대 너비를 설정 */
  width: 100%;
}

.row {
  --bs-gutter-x: 0;
}

.middle-container {
  display: flex;
  justify-content: space-around;
  padding: 30px 0;
  background-color: black;
  color: white;
  font-size: 20px;
  font-weight: 700;
}

.middle-item {
  color: white;
  text-align: center;
  width: 320px; /* 각 middle-item의 너비를 줄임 */
  height: 220px; /* 높이도 조정 */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 20px;
  cursor: pointer;
  background-size: cover; /* 이미지 크기를 덮도록 설정 */
  background-position: center; /* 이미지 위치를 가운데로 설정 */
  border: 2px solid white; /* 테두리 추가 */
}

.product {
  background-image: url('@/assets/img/home/home_button_1.jpg');
}

.map {
  background-image: url('@/assets/img/home/home_button_2.jpg');
}

.recommend {
  background-image: url('@/assets/img/home/home_button_3.jpg');
}

.bottom-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
  padding: 20px;
  background-color: black;
}

.notice-board {
  background-color: black;
  color: white;
}

@media (max-width: 1068px) {
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
