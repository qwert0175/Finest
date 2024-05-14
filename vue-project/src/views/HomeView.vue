<template>
    <div class="home row">
        <div class="top-container row">
            <div class="event-banner col-12 col-lg-9">
                <EventBanner />
            </div>
            <div class="exchange-calculator col-12 col-lg-3">
                <p>환율 계산기</p>
            </div>
        </div>
        <div class="middle-container d-flex">
            <div class="product-info">
                <p>상품정보 조회</p>
            </div>
            <div class="find-bank">
                <p>주변 은행 찾기</p>
            </div>
            <div class="recommend-product">
                <p>상품 추천 페이지</p>
            </div>
        </div>
        <div class="bottom-container d-flex">
            <div class="product-info">
                <p>공지사항</p>
            </div>
            <div class="find-bank">
                <p>자유 게시판</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import EventBanner from '@/components/EventBanner.vue';
import ExchangeCalculator from '@/components/ExchangeCalculator.vue';
</script>

<style scoped>
.top-container {
    /* background-color: red; */
    /* width: 100%; */
    height: 500px;
}

.event-banner {
}

.middle-container {
    background-color: blue;
    width: 100%;
    height: 300px;
}

.bottom-container {
    background-color: green;
    width: 100%;
    height: 250px;
}
</style>