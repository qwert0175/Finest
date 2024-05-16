<template>
  <div class="signup">
    <div class="comment">
      <p>창업을 준비하고 계신가요?</p>
      <p>Finest에서 정보를 얻고</p>
      <p>커뮤니티를 형성하세요!!</p>
    </div>
    <div class="signup-button-container">
      <div class="signup-button">
        <img src="@/assets/img/signup_finest.jpg" alt="signup_finest">
      </div>
      <div class="signup-button">
        <img src="@/assets/img/signup_google.jpg" alt="signup_google">
      </div>
      <div class="signup-button">
        <img src="@/assets/img/signup_kakao.jpg" alt="signup_kakao">
      </div>
    </div>
    <p>이미 회원이신가요? <a href="/login">로그인</a></p>
  </div>
</template>

<script setup>
</script>

<style scoped>
.signup {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  flex-direction: column;
}

.comment {
  margin: 100px 50px;
  font-size: 30px;
  font-weight: 700;
}

.signup-button {
  margin: 50px;
}
</style>
