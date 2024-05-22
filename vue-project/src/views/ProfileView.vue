<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">유저 프로필</p>
    </div>
    <div class="container">
      <div v-if="user" class="user-info">
        <h1>유저 정보</h1>
        <p><strong>아이디:</strong> {{ user.username }}</p>
        <p><strong>이메일:</strong> {{ user.email || '미등록' }}</p>
        <p><strong>연령:</strong> {{ user.age }}세</p>
        <p><strong>성별:</strong> {{ user.gender }}</p>
        <p><strong>월 수입:</strong> {{ user.salary }}</p>
        <p><strong>자산:</strong> {{ user.asset }}</p>
        <p><strong>부채:</strong> {{ user.debt }}</p>

        <div class="button-container">
          <button :class="{ active: currentTab === 'deposits' }" @click="currentTab = 'deposits'">예금</button>
          <button :class="{ active: currentTab === 'savings' }" @click="currentTab = 'savings'">적금</button>
        </div>

        <div v-if="currentTab === 'deposits'">
          <h2>가입한 예금상품</h2>
          <ul v-if="userDeposits.length > 0" class="product-list">
            <li v-for="deposit in userDeposits" :key="deposit.code" class="product-item">
              <RouterLink :to="{ name: 'depositdetail', params: { id: deposit.code } }">
                <div class="product-info">
                  <img :src="`src/assets/img/bank/${deposit.bank}.svg`" alt="은행 로고" class="bank-logo">
                  <div class="product-details">
                    <div class="product-bank">{{ deposit.bank }}</div>
                    <div class="product-name">{{ deposit.name }}</div>
                    <div class="product-rates">
                      <span class="base-rate">기본금리: {{ deposit.base_rate }}%</span>
                      <span class="max-rate">우대금리: {{ deposit.max_rate }}%</span>
                    </div>
                  </div>
                </div>
              </RouterLink>
            </li>
          </ul>
          <p v-else>가입한 예금상품이 없습니다.</p>
          <img v-if="recommendations && recommendations.deposit_interest_rate_graph && userDeposits.length > 0" 
               :src="'data:image/png;base64,' + recommendations.deposit_interest_rate_graph" 
               alt="User Deposit Interest Rates Graph" class="graph" />
        </div>

        <div v-if="currentTab === 'savings'">
          <h2>가입한 적금상품</h2>
          <ul v-if="userSavings.length > 0" class="product-list">
            <li v-for="saving in userSavings" :key="saving.code" class="product-item">
              <RouterLink :to="{ name: 'savingdetail', params: { id: saving.code } }">
                <div class="product-info">
                  <img :src="`src/assets/img/bank/${saving.bank}.svg`" alt="은행 로고" class="bank-logo">
                  <div class="product-details">
                    <div class="product-bank">{{ saving.bank }}</div>
                    <div class="product-name">{{ saving.name }}</div>
                    <div class="product-rates">
                      <span class="base-rate">기본금리: {{ saving.base_rate }}%</span>
                      <span class="max-rate">우대금리: {{ saving.max_rate }}%</span>
                    </div>
                  </div>
                </div>
              </RouterLink>
            </li>
          </ul>
          <p v-else>가입한 적금상품이 없습니다.</p>
          <img v-if="recommendations && recommendations.saving_interest_rate_graph && userSavings.length > 0" 
               :src="'data:image/png;base64,' + recommendations.saving_interest_rate_graph" 
               alt="User Saving Interest Rates Graph" class="graph" />
        </div>
      </div>
      <div v-if="loading" class="loading">로딩 중입니다.</div>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router';
import { useUserInfoStore } from '@/stores/userinfo';

const user = ref(null);
const userDeposits = ref([]);
const userSavings = ref([]);
const recommendations = ref(null);
const loading = ref(false);
const error = ref(null);
const userInfoStore = useUserInfoStore();

const currentTab = ref('deposits'); // Add a reactive variable to handle tab state

const router = useRouter();
const route = useRoute();

const fetchRecommendations = async () => {
  loading.value = true;
  try {
    if (!userInfoStore.token) { 
      error.value = '로그인이 필요합니다. 로그인 페이지로 이동합니다...';
      setTimeout(() => {
        router.push({ name: 'loginview' });  
      }, 2000);
      return;
    }

    // Fetch user data
    const userResponse = await axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/check/`,
      headers: {
          'Authorization': `Token ${userInfoStore.token}`
      }
    });
    const userData = userResponse.data;

    // Check if user has the required fields
    if (!userData.birthday || !userData.age || !userData.gender) {
      error.value = '회원 정보 수정 페이지에서 추가 정보를 입력해주세요. 입력 페이지로 이동합니다...';
      setTimeout(() => {
        router.push({ name: 'updateinfo' });
      }, 2000);
    } else {
      user.value = userData;

      // Fetch recommendations
      const response = await axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/product/graph/`,
          headers: {
              'Authorization': `Token ${userInfoStore.token}`
          }
      });
      const recommendationData = response.data;
      userDeposits.value = recommendationData.user_deposits;
      userSavings.value = recommendationData.user_savings;
      recommendations.value = recommendationData;
    }
  } catch (err) {
    error.value = '정보를 불러오는데 실패했습니다. 다시 시도해주세요';
  } finally {
    loading.value = false;
  }
};

onMounted(fetchRecommendations);
</script>

<style scoped>
.page-title {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000000; /* Orange color for the header */
  color: white;
  height: 50px;
  font-size: 20px;
}

.page-title-text {
  margin: 0;
}

.container {
  max-width: 1200px; /* Increase width for better view */
  margin: 0 auto;
  padding: 20px;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

.loading, .error {
  text-align: center;
  margin: 20px 0;
  font-size: 18px;
  color: #ff0000;
}

.user-info, .recommendations {
  margin-bottom: 30px;
  padding: 15px;
  background-color: #f2f2f2; /* Light gray background for info sections */
  border-radius: 8px;
}

h1, h2 {
  color: #333;
  margin-bottom: 15px;
  font-size: 24px;
}

.user-info > p {
  font-size: 16px;
  margin: 5px 0;
}

strong {
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

li {
  background-color: #fff;
  margin: 5px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  transition: background-color 0.3s;
}

li:hover {
  background-color: #f0f0f0;
}

.product-list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.product-item {
  display: flex;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}

.product-info {
  display: flex;
  align-items: center;
}

.bank-logo {
  width: 50px;
  height: 50px;
  margin-right: 15px;
}

.product-details {
  display: flex;
  flex-direction: column;
}

.product-name {
  font-weight: bold;
}

.product-bank {
  font-size: 14px;
  color: #999;
}

.product-rates {
  display: flex;
  gap: 10px;
}

.base-rate, .max-rate {
  font-size: 14px;
  color: #666;
}

.base-rate {
  color: #ff0000; /* 기본금리 색상 */
}

.max-rate {
  color: #00b300; /* 우대금리 색상 */
}

.graph {
  width: 100%;
  margin-top: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.button-container {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.button-container button {
  background-color: #e0e0e0; /* Slightly darker background for better visibility */
  border: none;
  padding: 10px 20px;
  margin: 0 10px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 5px;
  color: #666; /* Darker text color for better visibility */
  transition: background-color 0.3s, color 0.3s;
}

.button-container button:hover {
  background-color: #ccc; /* Darker hover background */
}

.button-container button.active {
  background-color: #007bff;
  color: white;
}
</style>
