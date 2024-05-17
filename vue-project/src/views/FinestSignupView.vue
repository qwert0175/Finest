<template>
    <div class="signup">
        <div class="title">
            <p>Finest 회원가입</p>
        </div>
        <form class="finest-signup-form" @submit.prevent="goToFinestSignUpView">
            <label for="username">이름</label>
            <input type="text" id="username" v-model.trim="username"><br>
            
            <label for="email">이메일</label>
            <input type="text" id="email" v-model.trim="email"><br>
            
            <label for="password1">비밀번호</label>
            <input type="password" id="password" v-model.trim="password1"><br>

            <label for="password2">비밀번호 확인</label>
            <input type="password" id="password-confirm" v-model.trim="password2">

            <input class="finest-signup-button" type="submit" value="Finest 가입하기">
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
  .signup {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    flex-direction: column;
  }
  
  .title {
    margin: 70px 50px;
    font-size: 50px;
    font-weight: 700;
  }

  .finest-signup-form {
    display: flex;
    flex-direction: column;
  }

  .finest-signup-button {
    margin-top: 100px;
    margin-bottom: 100px;
    font-size: 22px;
    font-weight: 700;
    color: white;
    background-color: #0064FF;
    border-radius: 10px;
    width: 416px;
    height: 50px;
    border: 0px;
  }

  input {
    border-radius: 4px;
  }
  </style>
  