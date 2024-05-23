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

            <label for="gender">성별(일부 서비스 이용 시 필요)</label>
            <select id="gender" v-model="userData.gender">
                <option value="남성">남성</option>
                <option value="여성">여성</option>
            </select><br>

            <label for="birthday">생일(일부 서비스 이용 시 필요)</label>
            <!-- <input type="date" id="birthday" v-model="userData.birthday"><br> -->
            <Datepicker locale="ko"
              class="datepicker"
              v-model="userData.birthday" 
              :enable-time-picker="false"
              :max-date="new Date()"
            /><br>

            <label for="salary">월 수입</label>
            <input type="number" min="0" max="999999999999" id="salary" v-model="userData.salary"><br>

            <label for="asset">보유 자산</label>
            <input type="number" min="0" max="999999999999" id="asset" v-model="userData.asset"><br>

            <label for="debt">부채</label>
            <input type="number" min="0" max="999999999999" id="debt" v-model="userData.debt"><br>
            <div class="button-container">
                <input class="finest-button update-userinfo" type="submit" value="회원 정보 수정">
                <input class="finest-button delete-userinfo" type="button" @click="withdrawal" value="회원 탈퇴">
            </div>
        </form>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import { useUserInfoStore } from '@/stores/userinfo';
import { useRouter } from 'vue-router';
import axios from 'axios'
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

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

const birthdayFormat = (birthday) => {
    if (!birthday) {
      return null
    } else {
      const birthDate = new Date(birthday)
      return `${birthDate.getFullYear()}-${birthDate.getMonth() + 1}-${birthDate.getDate()}`
    }
}

const withdrawal = () => {
    if (confirm('정말 탈퇴하시겠습니까?')) {
        axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/`,
            headers: {
                'Authorization': `Token ${userInfoStore.token}`
            }
        })
        .then(res => {
            alert('탈퇴되었습니다.')
            userInfoStore.username = null
            userInfoStore.token = null
            router.push({name: 'homeview'})
        })
        .catch(err => {
            for (const e in err.response.data) {
                alert(`${e}: ${err.response.data[e]}`)
            }
        })
    }
}

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
            birthday: birthdayFormat(res.data.birthday),
            salary: res.data.salary,
            asset: res.data.asset,
            debt: res.data.debt,
        }
    })
    .catch(err => {
        alert(err)
    })
})

const updateUserInfo = () => {
    const age = calculateAge(userData.value.birthday)
    axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/${userInfoStore.username}/`,
        headers: {
            'Authorization': `Token ${userInfoStore.token}`
        },
        data: {
            username: userData.value.username,
            email: userData.value.email || null,
            birthday: birthdayFormat(userData.value.birthday),
            age: age,
            gender: userData.value.gender || null,
            salary: userData.value.salary,
            asset: userData.value.asset,
            debt: userData.value.debt
        }
    })
    .then(res => {
        alert('회원 정보가 성공적으로 수정되었습니다.')
        router.push({name: 'homeview'})
    })
    .catch(err => {
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

.finest-button {
    font-size: 22px;
    font-weight: 700;
    color: white;
    background-color: #0064FF;
    border-radius: 10px;
    width: 416px;
    height: 50px;
    border: 0px;
}

.button-container {
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin-top: 30px;
    margin-bottom: 100px;
}

.update-userinfo {
    background-color: #0064FF;
}

.delete-userinfo {
    background-color: #ff0000;
}

input, select {
    border-radius: 4px;
    border: 2px solid  rgb(118, 118, 118);
    height: 24px;
}

.datepicker {
    border-radius: 7px;
    border: 2px solid  rgb(118, 118, 118);
}
</style>
