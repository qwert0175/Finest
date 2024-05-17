<template>
    <div class="login">
        <div class="title">
            <p>로그인</p>
        </div>
        <form class="login-form">
            <div class="input-container">
                <div class="label-text">Email Address</div>
                <input class="input-content" type="email" id="email" name="email" placeholder="이메일을 입력하세요">
            </div>
            <div class="input-container">
                <div class="label-text">Password</div>
                <input class="input-content" type="password" id="password" name="password" placeholder="패스워드를 입력하세요">
            </div>
            <a href="">Forgot Password?</a>
            <div class="button-container">
                <input type="submit" class="login-button" value="로그인">
                <RouterLink class="nav-link" to="/signupview">
                    <button class="signup-button">회원가입</button>
                </RouterLink>
            </div>
        </form>
    </div>
</template>

<script setup>
</script>

<style scoped>
.login {
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

.login-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
}

.login-form > a {
    margin-top: 10px;
}

.button-container {
    margin: auto;
    margin-top: 50px;
    display: flex;
    justify-content: space-around;
    width: 416px;
}

.login-button {
    color: white;
    background-color: #0064FF;
    border: 0px;
    width: 120px;
    height: 50px;
    font-weight: 700;
}

.signup-button {
    background-color: #FFFFFF;
    border: 1px solid #3751FE;
    width: 120px;
    height: 50px;
    font-weight: 700;
}

.input-container {
    position: relative;
    margin: 0 auto;
    font-family: Arial, sans-serif;
    width: 416px;
}

.label-text {
    position: absolute;
    top: 8px;
    left: 10px;
    font-size: 16px;
    color: #555;
}

.input-content {
    width: 100%;
    padding: 24px 8px 8px 8px; /* 위쪽에 여유 공간을 둠 */
    font-size: 16px;
    color: #3751FE;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
</style>
