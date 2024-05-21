<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">예금 상품 상세조회</p>
    </div>
    <div v-if="deposit" class="product-info">
      <div class="info-section">
        <p><strong>상품명:</strong> {{ deposit.fin_prdt_nm }}</p>
        <p><strong>은행명:</strong> {{ deposit.kor_co_nm }}</p>
        <p><strong>가입방법:</strong> {{ deposit.join_way }}</p>
        <p><strong>만기 후 이자율:</strong> {{ deposit.mtrt_int }}</p>
        <p><strong>우대조건:</strong> {{ deposit.spcl_cnd }}</p>
        <p v-if="deposit.join_deny === 1"><strong>가입제한:</strong> 제한없음</p> 
        <p v-else-if="deposit.join_deny === 2"><strong>가입제한:</strong> 서민전용</p> 
        <p v-else-if="deposit.join_deny === 3"><strong>가입제한:</strong> 일부제한</p> 
        <p><strong>가입대상:</strong> {{ deposit.join_member }}</p>
        <p><strong>최고한도:</strong> {{ deposit.max_limit || '없음' }}</p>
      </div>
      <div class="options-container">
        <div v-for="option in depositOptions" :key="option.save_trm" class="option-item">
          <button @click="setOptionState(option.save_trm)" :class="{ active: option.save_trm === optionState }">
            {{ option.save_trm }}개월
          </button>
        </div>
      </div>
      <div v-if="filteredOption" class="selected-option">
        <p><strong>금리 유형:</strong> {{ filteredOption.intr_rate_type_nm }}</p>
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
import axios from 'axios';

const route = useRoute();
const deposit = ref(null);
const depositOptions = ref([]);
const optionState = ref(null);

onMounted(() => {
  const depositId = route.params.id;
  axios.get(`http://127.0.0.1:8000/products/deposit/${depositId}/`)
    .then(res => {
      deposit.value = res.data.deposit;
      depositOptions.value = res.data.deposit_options;
      optionState.value = depositOptions.value[0].save_trm; // 기본 선택 값 설정
    })
    .catch(err => {
      console.error(err);
    });
});

const setOptionState = (saveTrm) => {
  optionState.value = saveTrm;
};

const filteredOption = computed(() => {
  return depositOptions.value.find(option => option.save_trm === optionState.value);
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

.options-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin: 20px 0;
  width: 100%;
}

.option-item {
  margin: 5px;
}

button {
  padding: 10px 20px;
  background-color: #3751FE;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button.active {
  background-color: #2a3cbf;
}

button:hover {
  background-color: #2a3cbf;
}

.selected-option {
  padding: 20px;
  background-color: #f9f9f9; /* 더 밝은 배경색 추가 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); /* 그림자 강도 조정 */
  border-radius: 10px;
  max-width: 800px;
  margin: 20px 0;
  width: 100%;
  border: 1px solid #ddd; /* 테두리 추가 */
}
</style>
