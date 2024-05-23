<template>
  <div>
    <div class="filters-container">
      <div class="filter-item">
        <label for="bankSelect">은행 검색</label>
        <select id="bankSelect" v-model="selectedBank">
          <option value="">모든 은행</option>
          <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
      </div>
      <div class="filter-item">
        <label for="periodSelect">기간</label>
        <select id="periodSelect" v-model="selectedPeriod">
          <option value="">모든 기간</option>
          <option value="1">1개월</option>
          <option value="3">3개월</option>
          <option value="6">6개월</option>
          <option value="12">12개월</option>
          <option value="24">24개월</option>
          <option value="36">36개월</option>
        </select>
      </div>
    </div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>금융회사명</th>
            <th>상품명</th>
            <th 
              class="sortable"
              :class="getSortClass('1')"
              @click="sortTable('1')">1개월
            </th>
            <th 
              class="sortable"
              :class="getSortClass('3')"
              @click="sortTable('3')">3개월
            </th>
            <th 
              class="sortable"
              :class="getSortClass('6')"
              @click="sortTable('6')">6개월
            </th>
            <th 
              class="sortable"
              :class="getSortClass('12')"
              @click="sortTable('12')">12개월
            </th>
            <th
              class="sortable"
              :class="getSortClass('24')"
              @click="sortTable('24')">24개월
            </th>
            <th 
              class="sortable"
              :class="getSortClass('36')"
              @click="sortTable('36')">36개월
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="saving in filteredAndSortedSavings" :key="saving.fin_prdt_cd">
            <td>{{ saving.kor_co_nm }}</td>
            <td>
              <router-link :to="{ name: 'savingdetail', params: { id: saving.fin_prdt_cd }}">
                {{ saving.fin_prdt_nm }}
              </router-link>
            </td>
            <td>{{ getRate(saving.fin_prdt_cd, 1) }}</td>
            <td>{{ getRate(saving.fin_prdt_cd, 3) }}</td>
            <td>{{ getRate(saving.fin_prdt_cd, 6) }}</td>
            <td>{{ getRate(saving.fin_prdt_cd, 12) }}</td>
            <td>{{ getRate(saving.fin_prdt_cd, 24) }}</td>
            <td>{{ getRate(saving.fin_prdt_cd, 36) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed } from 'vue';

const savings = ref([]);
const savingOptions = ref([]);
const sortOrder = ref({ column: null, ascending: true });
const selectedBank = ref('');
const selectedPeriod = ref('');

axios.get('http://127.0.0.1:8000/products/saving/')
  .then(response => {
    savings.value = response.data.savings
    savingOptions.value = response.data.saving_options
  })
  .catch(error => {
    console.error('Error:', error);
  });

function getInterestRates(fin_prdt_cd) {
  return savingOptions.value.filter(option => option.fin_prdt_cd === fin_prdt_cd);
}

function getRate(fin_prdt_cd, term) {
  const rates = getInterestRates(fin_prdt_cd);
  const rate = rates.find(rate => rate.save_trm == term);
  return rate ? rate.intr_rate : '-';
}

const sortedSavings = computed(() => {
  if (!sortOrder.value.column) return savings.value;

  const sorted = [...savings.value];
  sorted.sort((a, b) => {
    const rateA = getRate(a.fin_prdt_cd, sortOrder.value.column);
    const rateB = getRate(b.fin_prdt_cd, sortOrder.value.column);

    if (rateA === '-') return 1;
    if (rateB === '-') return -1;

    const valueA = parseFloat(rateA) || 0;
    const valueB = parseFloat(rateB) || 0;

    if (sortOrder.value.ascending) {
      return valueA - valueB;
    } else {
      return valueB - valueA;
    }
  });
  return sorted;
});


const filteredAndSortedSavings = computed(() => {
  return sortedSavings.value.filter(saving => {
    const matchesBank = selectedBank.value ? saving.kor_co_nm === selectedBank.value : true;
    const matchesPeriod = selectedPeriod.value ? getRate(saving.fin_prdt_cd, selectedPeriod.value) !== '-' : true;
    return matchesBank && matchesPeriod;
  });
});

function sortTable(column) {
  if (sortOrder.value.column === column) {
    sortOrder.value.ascending = !sortOrder.value.ascending;
  } else {
    sortOrder.value.column = column;
    sortOrder.value.ascending = true;
  }
}

function getSortClass(column) {
  if (sortOrder.value.column !== column) return '';
  return sortOrder.value.ascending ? 'sort-asc' : 'sort-desc';
}

const uniqueBanks = computed(() => {
  const banks = savings.value.map(saving => saving.kor_co_nm);
  return [...new Set(banks)];
});

</script>

<style scoped>
.table-container {
  width: 100%;
  overflow-x: auto;
  margin: 20px 0;
}

.filters-container {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
  margin-bottom: 20px;
}

.filter-item {
  display: flex;
  align-items: center;
}

.filter-item label {
  margin-right: 10px;
}

.filter-item select {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.filter-item button {
  margin-left: 10px;
  padding: 5px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.table-container {
  width: 100%;
  overflow-x: auto;
  margin: 20px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 0;
  padding: 0;
  table-layout: auto;
}

thead {
  background-color: #f5f5f5;
}

th, td {
  min-width: 42px;
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
}

th {
  background-color: #f0f0f0;
  font-weight: bold;
}

th.sortable:hover {
  cursor: pointer;
  background-color: #e0e0e0;
}

th.sortable::after {
  content: " \25B2";
  font-size: 0.8em;
  margin-left: 5px;
}

th.sortable.sort-desc::after {
  content: " \25BC";
}
</style>