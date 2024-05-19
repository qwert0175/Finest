<template>
    <div class="component">
      <div class="component-title">
        <p>환율 계산</p>
      </div>
      <div class="calculator">
        <div class="cur-container">
          <div class="form-floating">
            <select class="form-select" id="cur_1" aria-label="cur_1" v-model="cur1">
              <option selected>국가/통화</option>
              <option v-for="cur in exchangeInfo" :key="cur.cur_unit" :value="cur.cur_unit">{{cur.cur_nm}}</option>
            </select>
            <label for="cur_1">Amount</label>
          </div>
          <input class="form-control input-cur" type="number" v-model="amount" @input="exchange">
        </div>
        <div class="button-container">
          <div class="change-cur-button" @click="shiftChange">
            <img src="@/assets/img/change_cur_button.png" alt="change_cur_button">
          </div>
        </div>
        <div class="cur-container">
          <div class="form-floating">
            <select class="form-select" id="cur_2" aria-label="cur_2" v-model="cur2">
              <option selected>국가/통화</option>
              <option v-for="cur in exchangeInfo" :key="cur.cur_unit" :value="cur.cur_unit">{{cur.cur_nm}}</option>
            </select>
            <label for="cur_2">Converted Amount</label>
          </div>
          <input class="form-control input-cur" type="number" disabled :value="convertedAmount">
        </div>
        <div class="per-cur1">
          <p v-if="(cur1 !=='국가/통화') && (cur2 !== '국가/통화')">1 {{ cur1 }} = {{ (exchangeRate1 / exchangeRate2).toFixed(6) }} {{ cur2 }}</p>
          <p v-else>국가를 선택하세요.</p>
        </div>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, watch } from 'vue'
const exchangeInfo = ref(null)
axios.get('http://127.0.0.1:8000/exchanges/')
  .then(response => {
    exchangeInfo.value = response.data
  })
  .catch(error => {
    console.error('Error:', error);
  });

const amount = ref(0)
const convertedAmount = ref(0)
const cur1 = ref('국가/통화')
const cur2 = ref('국가/통화')
const exchangeRate1 = ref(0)
const exchangeRate2 = ref(0)
const exchange = () => {
  if (cur1.value !== '국가/통화' && cur2.value !== '국가/통화') {
    convertedAmount.value = amount.value*exchangeRate1.value/exchangeRate2.value
  }
}

watch([cur1, cur2], () => {
  amount.value = 0;
  convertedAmount.value = 0
  if (cur1.value !== '국가/통화' && cur2.value !== '국가/통화') {
    exchangeRate1.value = exchangeInfo.value.find(cur => cur.cur_unit === cur1.value).deal_bas_r
    exchangeRate2.value = exchangeInfo.value.find(cur => cur.cur_unit === cur2.value).deal_bas_r
  }
});

const shiftChange = () => {
  if (cur1.value !== '국가/통화' && cur2.value !== '국가/통화') {
    [cur1.value, cur2.value] = [cur2.value, cur1.value];
  } else {
    alert('국가를 선택하세요.')
  }
};
</script>

<style scoped>
.component {
  background-color: #F6F6F6;
  height: 100%;
  min-height: 300px;
}

.component-title {
  padding-top: 10px;
  text-align: center;
  color: #1F2261;
  font-size: 25px;
  font-weight: bold;
}

.calculator {
  background-color: white;
  border-radius: 20px;
  box-shadow: 0px 4px 4px #0000000d;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 20px;
  margin: 0 auto;
  margin-bottom: 20px;
  width: 80%;
}

@media (width: 1350px) {
  .calculator{
    min-height: 300px;
  }
}

.form-select {
  width: 150px;
}

.input-cur {
  width: 150px;
  height: 60px;
}

.per-cur1 {
  width: 100%;
  text-align: center;
}

.per-cur1 > p {
  margin: 0;
}

.cur-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 10px
}

.change-cur-button {
  position: relative;
  background-color: #25278d;
  width: 40px;
  height: 40px;
  text-align: center;
  border-radius: 50%;
}

.change-cur-button:active {
  background-color: red;
}

.change-cur-button > img {
  position: absolute;
  left: 12px;
  top: 11px;
  width: 16px;
  height: 18px;
}

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
</style>