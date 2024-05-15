<template>
    <div class="component">
      <div class="component-title">
        <p>환율 계산</p>
      </div>
      <div class="calculator">
        <div class="cur-container">
          <div class="form-floating">
            <select class="form-select" id="cur_1" aria-label="cur_1" v-model="cur1">
              <option selected>국가 1</option>
              <option v-for="cur in exchangeInfo" :key="cur.cur_unit" :value="cur.cur_unit">{{cur.cur_unit}}</option>
            </select>
            <label for="cur_1">Amount</label>
          </div>
          <input class="form-control input-cur" type="number" v-model="amount" @input="exchange">
        </div>
        <div class="cur-container">
          <div class="form-floating">
            <select class="form-select" id="cur_2" aria-label="cur_2" v-model="cur2">
              <option selected>국가 2</option>
              <option v-for="cur in exchangeInfo" :key="cur.cur_unit" :value="cur.cur_unit">{{cur.cur_unit}}</option>
            </select>
            <label for="cur_2">Converted Amount</label>
          </div>
          <input class="form-control input-cur" type="number" disabled :value="convertedAmount">
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
const cur1 = ref('국가 1')
const cur2 = ref('국가 2')
const exchange = () => {
  if (cur1.value !== '국가 1' && cur2.value !== '국가 2') {
    const exchangeRate1 = exchangeInfo.value.find(cur => cur.cur_unit === cur1.value).deal_bas_r
    const exchangeRate2 = exchangeInfo.value.find(cur => cur.cur_unit === cur2.value).deal_bas_r
    convertedAmount.value = amount.value*exchangeRate1/exchangeRate2
  }
}

watch([cur1, cur2], () => {
  amount.value = 0;
  convertedAmount.value = 0
});
</script>

<style scoped>
.component {
  background-color: #F6F6F6;
  border-radius: 20px;
  height: 100%;
  min-height: 300px;
}

.component-title {
  padding: 30px;
  text-align: center;
  color: #1F2261;
  font-size: 25px;
  font-weight: bold;
}

.calculator {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.form-select {
  width: 150px;
}

.input-cur {
  width: 150px;
  height: 60px;
}

.cur-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 10px
}
</style>