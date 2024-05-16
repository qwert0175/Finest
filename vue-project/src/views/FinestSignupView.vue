<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="goToFinestSignUpView">
        <label for="username">이름 : </label>
        <input type="text" id="username" v-model.trim="username"><br>
        
        <label for="email">이메일 : </label>
        <input type="text" id="email" v-model.trim="email"><br>
        
        <label for="password1">비밀번호 : </label>
        <input type="text" id="password1" v-model.trim="password1"><br>

        <label for="password2">비밀번호 확인 : </label>
        <input type="text" id="password2" v-model.trim="password2">

        <input type="submit" value="제출">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const router = useRouter()

const goToFinestSignUpView = function () {
    axios ({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: {
            username: username.value,
            email: email.value,
            password1: password1.value,
            password2: password2.value
        }
    })
        .then(res => {
            console.log('회원가입 성공')
            router.push({name: 'homeview'})
        })
        .catch(err => {
            console.log('회원가입 실패')
            alert('에러')
        })
}
</script>

<style scoped>
</style>
