<template>
    <div class="signup">
        <div class="title">
            <p>Finest 회원정보 수정</p>
        </div>
        <form class="finest-signup-form" @submit.prevent="updateUserInfo">
            <label for="username">아이디(10자 제한)</label>
            <input type="text" id="username" maxlength="10" v-model.trim="userData.username" disabled><br>
            
            <label for="email">이메일</label>
            <input type="text" id="email" v-model="userData.email"><br>

            <label for="gender">성별</label>
            <select id="gender" v-model="userData.gender">
                <option value="남성">남성</option>
                <option value="여성">여성</option>
            </select><br>

            <label for="birthday">생일</label>
            <input type="date" id="birthday" v-model="userData.birthday"><br>

            <label for="salary">월 수입</label>
            <input type="number" min="0" max="999999999999" id="salary" v-model="userData.salary"><br>

            <label for="asset">보유 자산</label>
            <input type="number" min="0" max="999999999999" id="asset" v-model="userData.asset"><br>

            <label for="debt">부채</label>
            <input type="number" min="0" max="999999999999" id="debt" v-model="userData.debt"><br>

            <input class="finest-signup-button" type="submit" value="회원 정보 수정">
        </form>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo';
import { useRouter } from 'vue-router';
import axios from 'axios'
const router = useRouter()
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
    debt: ''
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
        console.log(res)
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
        console.log(err)
        for (const e in err.response.data) {
            alert(`${e}: ${err.response.data[e]}`)
        }
    })
})

const updateUserInfo = () => {
    axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        },
        data: userData.value
    })
    .then(res => {
        alert('회원 정보가 성공적으로 수정되었습니다.')
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
