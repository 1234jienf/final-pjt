<template>
    <div class="main">
      <div class="left-content">
        <!-- 로고 이미지를 포함한 컨텐츠 -->
        <div class="logo">
          <img src="@/assets/img/main/sdfsdfdsf-removebg-preview.png" alt="Logo">
        </div>
      </div>
      <h1 class="welcome-text">Welcome to Freddit</h1>
      <div class="down-logo" @click="scrollDown">
      <font-awesome-icon :icon="['fas', 'chevron-down']" bounce/>
    </div>
      <div ref="content" class="right-content">
        <!-- 오른쪽 컨텐츠 -->
        <h3>OUR SERVICES</h3>
        <div class="box-container">
          <!-- 박스들 -->
          <div class="box">
            <RouterLink :to="{ name: 'DepositView' }" class="nav-link btn-2">정기 예금/적금</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'CalculatorView' }" class="nav-link btn-2">환율 계산기</RouterLink>
          </div>
          <div class="box">금융상품 추천</div>
          <div class="box">
            <RouterLink :to="{ name: 'KakaomapView' }" class="nav-link btn-2">지도보기</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'BoardView' }" class="nav-link btn-2">커뮤니티</RouterLink>
          </div>
        </div>
      </div>
    </div>


  </template>
<script>
import { library } from '@fortawesome/fontawesome-svg-core';
import { far } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(far);

export default {
  components: {
    FontAwesomeIcon // 컴포넌트를 등록합니다.
  },
  methods: {
    scrollDown() {
      // 클릭 시 스크롤을 아래로 이동
      this.$refs.content.scrollIntoView({ behavior: 'smooth' });
    }
  }
}
</script>
  <style scoped>
  .main {
  display: flex;
  background-color: #526ADF;
  flex-direction: column;
  height: 150vh;
}

.left-content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  background-color: #EAEFFE;
  color: white;
}

/* 로고 이미지 스타일 */
.logo img {
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin: auto;
}
.welcome-text {
    margin-top: 100px;
    text-align: center; /* 텍스트 중앙 정렬 */
  color: white; /* 글자색 변경 */
}

.right-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex: 3;
  color: white;
}
  .box-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
    justify-content: center;
  } 

  .box {
    width: 150px;
    height: 150px;
    background-color: #c2dfff;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border-radius: 10px; /* 원하는 값으로 조정 */
    color: #526ADF;
    box-shadow: -5px -5px 20px #FFF, 5px 5px 20px #BABECC;
    transition: all 0.2s ease-in-out;
  }
.box:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
  border-radius: 10px; /* hover 시 둥글게 조정되도록 설정 */
  transform: scale(1.1); /* 확대 효과 */
  color: white; /* 글자색 변경 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* 그림자 효과 */
}
  .down-logo {
    margin-top: 50px;
    margin-bottom: 50px; /* 이동된 위치를 제어하기 위해 margin-top을 auto로 설정합니다. */
    align-self: center; /* 수직 가운데 정렬을 위해 중앙 정렬합니다. */
}
  </style>
