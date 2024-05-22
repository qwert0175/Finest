<template>
  <div class="container">
    <div v-if="loading" class="loading">로딩 중입니다.</div>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="user" class="user-info">
      <h1>User Information</h1>
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Age:</strong> {{ user.age }}</p>
      <p><strong>Gender:</strong> {{ user.gender }}</p>

      <!-- 예금 정보 출력 -->
      <h2>가입한 예금상품</h2>
      <ul>
        <RouterLink
          v-for="deposit in user.deposits"
          :key="deposit.code"
          :to="{ name: 'depositdetail', params: { id: deposit.code } }">
          <li>
            {{ deposit.name }} ({{ deposit.code }})
          </li>
        </RouterLink>
      </ul>

      <!-- 적금 정보 출력 -->
      <h2>가입한 적금상품</h2>
      <ul>
        <RouterLink
          v-for="saving in user.savings"
          :key="saving.code"
          :to="{ name: 'savingdetail', params: { id: saving.code } }">
          <li>
            {{ saving.name }} ({{ saving.code }})
          </li>
        </RouterLink>
      </ul>
    </div>
    <div v-if="recommendations" class="recommendations">
      <h2>추천 예금상품</h2>
      <ul>
        <RouterLink
          v-for="deposit in recommendations.top_deposits"
          :key="deposit.code"
          :to="{ name: 'depositdetail', params: { id: deposit.code } }">
          <li>
            {{ deposit.name }}
          </li>
        </RouterLink>
      </ul>
      <img :src="'data:image/png;base64,' + recommendations.deposit_graph" alt="Top Deposits Graph" class="graph" />
      
      <h2>추천 적금상품</h2>
      <ul>
        <RouterLink
          v-for="saving in recommendations.top_savings"
          :key="saving.code"
          :to="{ name: 'savingdetail', params: { id: saving.code } }">
          <li>
            {{ saving.name }}
          </li>
        </RouterLink>
      </ul>
      <img :src="'data:image/png;base64,' + recommendations.saving_graph" alt="Top Savings Graph" class="graph" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router';
import { useUserInfoStore } from '@/stores/userinfo';

const user = ref(null);
const recommendations = ref(null);
const loading = ref(false);
const error = ref(null);
const userInfoStore = useUserInfoStore();

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
          url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/product/recommend/`,
          headers: {
              'Authorization': `Token ${userInfoStore.token}`
          }
      });
      recommendations.value = response.data;
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
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.loading, .error {
  text-align: center;
  margin: 20px 0;
  font-size: 18px;
  color: #ff0000;
}

.user-info, .recommendations {
  margin-bottom: 30px;
}

h1, h2 {
  color: #333;
  margin-bottom: 15px;
}

p {
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
  background-color: #f9f9f9;
  margin: 5px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  transition: background-color 0.3s;
}

li:hover {
  background-color: #f0f0f0;
}

.graph {
  width: 100%;
  margin-top: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
