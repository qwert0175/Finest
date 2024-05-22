<template>
    <div>
        <p>{{ userData.username }}님의 페이지</p>
        <p>이메일: {{ userData.email }}</p>
        <p>성별: {{ userData.gender }}</p>
        <p>생일: {{ userData.birthday }}</p>
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