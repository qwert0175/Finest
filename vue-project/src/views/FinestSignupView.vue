<template>
    <div class="signup">
        <div class="title">
            <p>Finest 회원가입</p>
        </div>
        <form class="finest-signup-form" @submit.prevent="goToFinestSignUpView">
            <label for="username">아이디(10자 제한)</label>
            <input type="text" id="username" maxlength="10" v-model.trim="username"><br>
            
            <label for="email">이메일</label>
            <input type="text" id="email" v-model="email"><br>
            
            <label for="password1">비밀번호(8자~15자 이내)</label>
            <input type="password" id="password1" maxlength="15" v-model.trim="password1"><br>

            <label for="password2">비밀번호 확인</label>
            <input type="password" id="password2" maxlength="15" v-model.trim="password2"><br>

            <label for="gender">성별</label>
            <select id="gender" v-model="gender">
                <option value="남성">남성</option>
                <option value="여성">여성</option>
            </select><br>

            <label for="birthday">생일</label>
            <input type="date" id="birthday" v-model="birthday"><br>

            <label for="salary">월 수입</label>
            <input type="number" min="0" max="999999999999" id="salary" v-model="salary"><br>

            <label for="asset">보유 자산</label>
            <input type="number" min="0" max="999999999999" id="asset" v-model="asset"><br>

            <label for="debt">부채</label>
            <input type="number" min="0" max="999999999999" id="debt" v-model="debt"><br>

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
  const gender = ref(null)
  const birthday = ref(null)
  const salary = ref(0)
  const asset = ref(0)
  const debt = ref(0)
  
  const router = useRouter()

  const calculateAge = (birthday) => {
    if (!birthday) {
      return null
    } else {
      const birthDate = new Date(birthday)
      const today = new Date()
      let age = today.getFullYear() - birthDate.getFullYear()
      const monthDifference = today.getMonth() - birthDate.getMonth()
      if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
          age--
      }
      return age
  }
  }
  
  const goToFinestSignUpView = function () {
    const age = calculateAge(birthday.value)
    console.log(age)
    axios ({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/accounts/registration/',
      data: {
        username: username.value,
        email: email.value || null,
        password1: password1.value,
        password2: password2.value,
        birthday: birthday.value || null,
        age: age || null,
        gender: gender.value || null,
        salary: salary.value,
        asset: asset.value,
        debt: debt.value
      }
    })
    .then(res => {
      console.log(res)
      router.push({name: 'homeview'})
    })
    .catch(err => {
      console.log(err)
      for (const e in err.response.data) {
        alert(`${e}: ${err.response.data[e]}`)
      }
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

  input, select {
    border-radius: 4px;
    border: 2px solid  rgb(118, 118, 118);
    height: 24px;
  }
  </style>
  