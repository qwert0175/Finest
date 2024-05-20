<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <!-- <a class="navbar-brand" href="#">Navbar</a> -->
    <RouterLink class="navbar-brand" to="/">Finest</RouterLink>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink class="nav-link" to="/mapview">은행지도</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/communityview">커뮤니티</RouterLink>
        </li>
      </ul>
      <div class="d-flex">
        <ul v-if="userInfoStore.token" class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
              <RouterLink class="nav-link" to="/updateview">회원정보수정</RouterLink>
          </li>
          <li class="nav-item">
              <a class="nav-link" @click="logOut">로그아웃</a>
          </li>
        </ul>
        <ul v-else class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
              <RouterLink class="nav-link" to="/loginview">로그인</RouterLink>
          </li>
          <li class="nav-item">
              <RouterLink class="nav-link" to="/signupview">회원가입</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>
    </div>
</template>

<script setup>
import { useUserInfoStore } from '@/stores/userinfo';
import axios from 'axios';
const userInfoStore = useUserInfoStore();

const logOut = () => {
  axios ({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/accounts/logout/',
    })
    .then(res => {
      console.log(res)
      userInfoStore.token = null;
    })
    .catch(err => {
      console.log(err)
      for (const e in err.response.data) {
        alert(err.response.data[e])
      }
    })
  }
</script>

<style scoped>
.nav-link:hover {
  cursor: pointer
}
</style>