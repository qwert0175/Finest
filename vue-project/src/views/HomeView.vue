<template>
    <div class="home row">
        <div class="top-container row">
            <div class="event-banner col-12 col-lg-9 p-0">
                <EventBanner />
            </div>
            <div class="exchange-calculator col-12 col-lg-3 p-0 pr-0">
                <ExchangeCalculator />
            </div>
        </div>
        <div class="middle-container d-flex">
            <div class="middle-item">
                <p>상품정보 조회</p>
            </div>
            <RouterLink class="nav-link" to="/mapview">
                <div class="middle-item"> 
                    <p>주변은행 찾기</p>
                </div>
            </RouterLink>
            <div class="middle-item">
                <p>상품 추천 페이지</p>
            </div>
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
    padding: 0;
}

.middle-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin: 30px 0px 30px 0px;
}

.middle-item {
    color: white;
    background-color: #1F2261;
    text-align: center;
    align-content: center;
    width: 250px;
    height: 200px;
    border-radius: 20px;
}

.middle-item p {
    margin: 0
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