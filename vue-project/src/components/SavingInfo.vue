<template>
    <div class="product-container">
        <div class="product-container" v-for="saving in savings">
            <p>{{ saving.fin_prdt_nm }}</p>
            <p>{{ saving.kor_co_nm }}</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'

const savings = ref(null)
const savingOptions = ref(null)
axios.get('http://127.0.0.1:8000/products/saving/')
  .then(response => {
    savings.value = response.data.savings
    savingOptions.value = response.data.saving_options
  })
  .catch(error => {
    console.error('Error:', error);
  });
</script>

<style scoped>
</style>