<template>
    <div>
        <p>{{ userData.username }}님의 페이지</p>
        <p>이메일: {{ userData.email }}</p>
        <p>성별: {{ userData.gender }}</p>
        <p>생일: {{ userData.birthday }}</p>
        <p>월 수입: {{ userData.salary }}</p>
        <p>자산: {{ userData.asset }}</p>
        <p>부채: {{ userData.debt }}</p>
        <p>가입한 예금 정보</p>
        <ul>
            <li v-for="deposit in userProducts.deposits">{{ deposit.deposit }}</li>
        </ul>
        <p>가입한 적금 정보</p>
        <ul>
            <li v-for="saving in userProducts.savings">{{ saving.saving }}</li>
        </ul>
        <p>가입 대출</p>
        <ul>
            
        </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo';
import axios from 'axios';
const userInfoStore = useUserInfoStore()
const userData = ref({
    username: '',
    email: '',
    password1: '',
    password2: '',
    gender: '',
    birthday: '',
    salary: '',
    asset: '',
    debt: '',
})
const userProducts = ref({
    deposits: [],
    savings: [],
    creditloan: [],
})

onMounted(() => {
    axios ({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        }
    })
    .then(res => {
        userData.value = {
            username: res.data.username,
            email: res.data.email,
            gender: res.data.gender,
            birthday: res.data.birthday,
            salary: res.data.salary,
            asset: res.data.asset,
            debt: res.data.debt,
        }
    })
    .catch(err => {
        alert(err)
    })

    axios ({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/product/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        }
    })
    .then(res => {
        userProducts.value = {
            deposits: res.data.deposits,
            savings: res.data.savings,
            creditloan: res.data.creditloan,
        }
    })
    .catch(err => {
        alert(err)
    })
})
</script>

<style scoped>

</style>