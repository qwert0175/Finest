<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">예금 상품 상세조회</p>
    </div>
    <div v-if="saving" class="product-info">
      <div class="info-section">
        <p><strong>상품명:</strong> {{ saving.fin_prdt_nm }}</p>
        <p><strong>은행명:</strong> {{ saving.kor_co_nm }}</p>
        <p><strong>가입방법:</strong> {{ saving.join_way }}</p>
        <p><strong>만기 후 이자율:</strong> {{ saving.mtrt_int }}</p>
        <p><strong>우대조건:</strong> {{ saving.spcl_cnd }}</p>
        <p v-if="saving.join_deny === 1"><strong>가입제한:</strong> 제한없음</p> 
        <p v-else-if="saving.join_deny === 2"><strong>가입제한:</strong> 서민전용</p> 
        <p v-else-if="saving.join_deny === 3"><strong>가입제한:</strong> 일부제한</p> 
        <p><strong>가입대상:</strong> {{ saving.join_member }}</p>
        <p><strong>최고한도:</strong> {{ saving.max_limit || '없음' }}</p>
      </div>
      <button @click="subscribe" :class="{ 'unsubscribe-button': isSubscribed }">
        {{ isSubscribed ? '탈퇴하기' : '가입하기' }}
      </button>
      <div v-for="(options, type) in groupedSavingOptions" :key="type" class="options-group">
        <div class="options-group-title">{{ type }}</div>
        <div class="options-container">
          <div v-for="option in options" :key="option.rsrv_type_nm + option.save_trm" class="option-item">
            <button @click="setOptionState(option.rsrv_type_nm, option.save_trm)" :class="{ active: option.rsrv_type_nm === optionState.type && option.save_trm === optionState.term }">
              {{ option.save_trm }}개월
            </button>
          </div>
        </div>
      </div>
      <div v-if="filteredOption" class="selected-option">
        <p><strong>금리 유형:</strong> {{ filteredOption.intr_rate_type_nm }}</p>
        <p><strong>저축 유형:</strong> {{ filteredOption.rsrv_type_nm }}</p>
        <p><strong>기간:</strong> {{ filteredOption.save_trm }}개월</p>
        <p><strong>이자율:</strong> {{ filteredOption.intr_rate }}%</p>
        <p><strong>최고 우대금리:</strong> {{ filteredOption.intr_rate2 }}%</p>
      </div>
    </div>
    <div v-else class="loading">
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useUserInfoStore } from '@/stores/userinfo';
import axios from 'axios';

const route = useRoute();
const saving = ref(null);
const savingOptions = ref([]);
const optionState = ref({ type: null, term: null });
const userInfoStore = useUserInfoStore();
const isSubscribed = ref(false);

onMounted(() => {
  const savingId = route.params.id;
  axios.get(`http://127.0.0.1:8000/products/saving/${savingId}/`)
    .then(res => {
      saving.value = res.data.saving;
      savingOptions.value = res.data.saving_options.sort((a, b) => a.save_trm - b.save_trm); // save_trm 기준으로 정렬
      optionState.value = {
        type: savingOptions.value[0].rsrv_type_nm,
        term: savingOptions.value[0].save_trm
      }; // 기본 선택 값 설정
      checkSubscription();
    })
    .catch(err => {
      console.error(err);
    });
});

const checkSubscription = () => {
  axios.get(`http://127.0.0.1:8000/accounts/${userInfoStore.username}/saving/check/${saving.value.fin_prdt_cd}/`, {
    headers: {
      'Authorization': `Token ${userInfoStore.token}`
    }
  })
  .then(res => {
    const userProducts = res.data;
    isSubscribed.value = userProducts.is_subscribed;

  })
  .catch(err => {
    console.error(err);
  });
};

const subscribe = () => {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/accounts/saving/',
    headers: {
      'Authorization': `Token ${userInfoStore.token}`
    },
    data: {
      username: userInfoStore.username,
      fin_prdt_cd: saving.value.fin_prdt_cd
    },
  })
  .then(res => {
    isSubscribed.value = !isSubscribed.value;
    console.log(res.data);
  })
  .catch(err => {
    console.error(err);
  });
};

const setOptionState = (type, term) => {
  optionState.value = { type, term };
};

const filteredOption = computed(() => {
  return savingOptions.value.find(option => option.rsrv_type_nm === optionState.value.type && option.save_trm === optionState.value.term);
});

const groupedSavingOptions = computed(() => {
  return savingOptions.value.reduce((groups, option) => {
    const type = option.rsrv_type_nm;
    if (!groups[type]) {
      groups[type] = [];
    }
    groups[type].push(option);
    return groups;
  }, {});
});
</script>

<style scoped>
.page-title {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #3751FE;
  height: 50px;
  font-size: 20px;
  color: white;
}

.page-title-text {
  margin: 0;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  font-size: 18px;
}

.product-info {
  padding: 20px;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  margin: 20px 0;
  max-width: 800px;
  margin: 20px auto;
  line-height: 1.6;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.info-section {
  width: 100%;
  margin-bottom: 20px;
}

.options-group {
  margin-bottom: 20px;
  text-align: center;
}

.options-group-title {
  font-weight: bold;
  margin-bottom: 10px;
}

.options-container {
  display: flex;
  justify-content: center; /* 중앙 정렬 */
  flex-wrap: wrap; /* 여러 줄로 나누어 표시 */
  margin: 10px 0;
}

.option-item {
  margin: 5px;
}

button {
  padding: 10px 20px; /* 버튼 패딩 조정 */
  background-color: #3751FE;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button.active {
  background-color: #2a3cbf; /* 활성 버튼 배경색 변경 */
}

button:hover {
  background-color: #2a3cbf; /* 호버 시 배경색 변경 */
}

button.unsubscribe-button {
  background-color: #FF0000;
}

button.unsubscribe-button:hover {
  background-color: #CC0000;
}

.selected-option {
  padding: 20px;
  background-color: #f9f9f9; /* 더 밝은 배경색 추가 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* 그림자 강도 조정 */
  border-radius: 10px;
  max-width: 800px;
  margin: 20px auto;
  width: 100%;
  border: 1px solid #ddd; /* 테두리 추가 */
}
</style>
