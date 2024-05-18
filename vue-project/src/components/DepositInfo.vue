<template>
    <div class="product-container">
        <div class="product-item" v-for="deposit in deposits">
            <p>{{ deposit.fin_prdt_nm }}</p>
            <p>{{ deposit.kor_co_nm }}</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'

const deposits = ref(null)
const depositOptions = ref(null)
axios.get('http://127.0.0.1:8000/products/deposit/')
  .then(response => {
    deposits.value = response.data.deposits
    depositOptions.value = response.data.deposit_options
  })
  .catch(error => {
    console.error('Error:', error);
  });
</script>

<style scoped>
</style>