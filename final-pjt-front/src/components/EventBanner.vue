<template>
    <div class="banner">
        <div id="carouselExampleIndicators" class="carousel slide">
            <div class="carousel-overlay"></div>
            <div class="carousel-inner pt-4">
                <div class="carousel-item active">
                    <img src="@/assets/img/banner/banner1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/img/banner/banner4.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/img/banner/banner2.jpg" class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
        </div>
    </div>
</template>

<script setup>
</script>

<style scoped>
.banner {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

#carouselExampleIndicators {
    width: 100%;
    overflow: hidden; /* 이미지가 컨테이너의 경계를 넘어서는 부분을 숨깁니다 */
}

.carousel-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7); /* 반투명 검은색 배경 */
    z-index: 0;
}

.carousel-inner, .carousel-indicators {
    position: relative;
    z-index: 1; /* 이미지와 인디케이터가 오버레이 위에 보이도록 설정 */
}

.carousel-control-prev, .carousel-control-next {
    z-index: 2; /* 버튼이 가장 위에 오도록 설정 */
}

.carousel-item img {
    display: block;
    max-width: 720px;
    /* max-height: 400px; */
    width: auto; /* 자동 너비 조정 */
    margin: auto;
    object-fit: contain; /* 콘텐츠 비율을 유지하며 채웁니다 */
}
</style>