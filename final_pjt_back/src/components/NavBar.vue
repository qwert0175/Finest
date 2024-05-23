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
          <RouterLink class="nav-link" to="/product">금리 비교</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/mapview">은행 찾기</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/recommendview">추천 상품</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/communityview">게시판</RouterLink>
        </li>
      </ul>
      <div class="d-flex">
        <ul v-if="userInfoStore.token" class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
              <RouterLink class="nav-link" to="/profile">{{ userInfoStore.username }}</RouterLink>
          </li>
          <li class="nav-item">
              <RouterLink class="nav-link" to="/updateinfo">회원정보수정</RouterLink>
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
import { useRouter } from 'vue-router';
const router = useRouter();
const userInfoStore = useUserInfoStore();

const logOut = () => {
  axios ({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/accounts/logout/',
    })
    .then(res => {
      userInfoStore.token = null;
      userInfoStore.name = null;
      router.push({name: 'homeview'})
    })
    .catch(err => {
      console.log(err)
      // for (const e in err.response.data) {
      //   alert(err.response.data[e])
      // }
    })
  }
</script>

<style scoped>
.nav-link:hover {
  cursor: pointer
}
</style>