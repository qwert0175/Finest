<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">예적금 금리 비교</p>
    </div>
    <div class="choose-product">
      <button :class="{onSelected: userinfoStore.isDeposit}" @click="userinfoStore.isDeposit = true">예금</button>
      <button :class="{onSelected: !userinfoStore.isDeposit}" @click="userinfoStore.isDeposit = false">적금</button>
    </div>
    <div class="product-section">
      <DepositInfo v-if="userinfoStore.isDeposit" />
      <SavingInfo v-else/>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import DepositInfo from '@/components/DepositInfo.vue'
import SavingInfo from '@/components/SavingInfo.vue'
import { useUserInfoStore } from '@/stores/userinfo';
const userinfoStore = useUserInfoStore()
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

.choose-product {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px;
}

.choose-product {
  button {
    width: 100px;
    height: 50px;
    margin: 10px;
    border: 0px;
    border-radius: 10px;
  }

  .onSelected {
    background-color: #3751FE;
    color: white;
  }
}

.product-section {
  margin: 20px;
}
</style>