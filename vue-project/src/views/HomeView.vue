<template>
    <div class="home row">
        <div class="top-container row">
            <div class="event-banner col-12 col-lg-8 p-0">
                <EventBanner />
            </div>
            <div class="exchange-calculator col-12 col-lg-4 p-0">
                <ExchangeCalculator />
            </div>
        </div>
        <div class="middle-container d-flex">
            <RouterLink class="nav-link" to="/product">
                <div class="middle-item product">
                    <p>상품정보 조회</p>
                </div>
            </RouterLink>
            <RouterLink class="nav-link" to="/mapview">
                <div class="middle-item map"> 
                    <p>주변은행 찾기</p>
                </div>
            </RouterLink>
            <RouterLink class="nav-link" to="/recommendview">
                <div class="middle-item recommend">
                    <p>상품 추천 페이지</p>
                </div>
            </RouterLink>
        </div>
        <div class="bottom-container d-flex">
            <div class="product-info">
                <p>공지사항</p>
            </div>
            <div class="find-bank">
                <p>자유게시판</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import EventBanner from '@/components/EventBanner.vue';
import ExchangeCalculator from '@/components/ExchangeCalculator.vue';
</script>

<style scoped>
.row {
    --bs-gutter-x: 0;
}

.middle-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin: 30px 0px 30px 0px;
}

.middle-item {
    color: white;
    /* background-color: #1F2261; */
    text-align: center;
    align-content: center;
    width: 250px;
    height: 200px;
}

.middle-item p {
    margin: 0
}

.product {
    background-color: #3751FE;
    border-radius: 20px;
}

.map {
    background-color: #E47643;
    border-radius: 20px;
}

.recommend {
    background-color: black;
    border-radius: 20px;
}

.bottom-container {
    background-color: green;
    width: 100%;
    height: 250px;
}

@media (max-width: 768px) {
    .middle-container {
        flex-direction: column;
        align-items: center;
    }

    .middle-item {
        margin-bottom: 20px;
    }
}
</style>