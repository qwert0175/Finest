<template>
  <div>
    <div class="page-title">
      <p class="page-title-text">예적금 금리 비교</p>
    </div>
    <div class="">
      <DepositInfo />
      <SavingInfo />
    </div>
  </div>
</template>

<script setup>
import DepositInfo from '@/components/DepositInfo.vue'
import SavingInfo from '@/components/SavingInfo.vue'
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

</style>