<template>
  <div class="main">
    <div class="left-content">
      <!-- 로고 이미지를 포함한 컨텐츠 -->
      <div class="logo">
        <img src="@/assets/img/main/sdfsdfdsf-removebg-preview.png" alt="Logo">
      </div>
    </div>
    <div class="down-logo" @click="scrollDown">
      <button class="btn">Freddit 구경가기</button>
    </div>
    <div class="container">
      <div class="card">
        <h1 class="title">Welcome to Freddit</h1>
        <p class="subtitle">이제 설명 적어야함..</p>
        <button class="btn2" @click="scrollDown">
          <RouterLink :to="{ name: 'SignUpView' }" class="btn-2">
          Freddit 가입하기
        </RouterLink>
      </button>
      </div>
      <div class="blob"></div>
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
  height: auto; /* 변경 */
  min-height: 100vh; /* 화면 높이 최소값 */
  overflow: auto; /* 스크롤이 필요할 때 스크롤 표시 */
  position: relative; /* 화면에 꽉 차도록 */
  padding-bottom: 50px; /* 하단 여백 추가 */
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
  width: 200px;
  height: 200px;
  background-color: #c2dfff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  border-radius: 10px; /* 원하는 값으로 조정 */
  color: #526ADF;
  transition: all 0.2s ease-in-out;
}

 /* .box {
max-width: 150px;
min-height: 150px;
display: flex;
flex-direction: column;

justify-content: center;
padding: 35px;
border: 1px solid rgba(255, 255, 255, .25);
border-radius: 10px;
background-color: rgba(255, 255, 255, 0.45);
box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.25);
box-shadow: -5px -5px 20px #FFF, 5px 5px 20px #BABECC; 
backdrop-filter: blur(15px);
} */ 

.box:hover {
box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
border-radius: 15px; /* hover 시 둥글게 조정되도록 설정 */
transform: scale(1.1); /* 확대 효과 */
color: white; /* 글자색 변경 */
box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* 그림자 효과 */
}
.down-logo {
  margin-top: 50px;
  margin-bottom: 80px; /* 이동된 위치를 제어하기 위해 margin-top을 auto로 설정합니다. */
  align-self: center; /* 수직 가운데 정렬을 위해 중앙 정렬합니다. */
}

* {
	box-sizing: border-box;
	margin: 0;
	padding: 0;
	font-family: "Nunito", sans-serif;
}

body {
  background: #1f1f47
}

.container {
  min-height: 95vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.card {
  width: 400px;
  min-height: 250px;
  background: rgba( 255, 255, 255, 0.15 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 18px );
  -webkit-backdrop-filter: blur( 18px );
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 1rem;
  padding: 1.5rem;
  z-index: 10;
  color: whitesmoke;
}

.title {
  font-size: 2.2rem;
  margin-bottom: 1rem;
}

.subtitle {
  font-size: 1rem;
  margin-bottom: 2rem;
}

.btn2 {
  background: none;
  border: none;
  text-align: center;
  font-size: 1rem;
  color: whitesmoke;
  background-color: #fa709a;
  padding: 0.8rem 1.8rem;
  border-radius: 2rem;
  cursor: pointer;
}
.btn {
  background: none;
  border: none;
  text-align: center;
  font-size: 1rem;
  color: whitesmoke;
  background-color: #1f1f47;
  padding: 0.8rem 1.8rem;
  border-radius: 2rem;
  cursor: pointer;
}

.blob {
  position: absolute;
  width: 500px;
  height: 500px;
  background: linear-gradient(
    180deg,
    rgba(47, 184, 255,0.42) 31.77%,
    #5c9df1 100%
  );
  mix-blend-mode: color-dodge;
  -webkit-animation: move 25s infinite alternate;
          animation: move 25s infinite alternate;
  transition: 1s cubic-bezier(0.07, 0.8, 0.16, 1);
}

.blob:hover {
  width: 520px;
  height: 520px;
  -webkit-filter: blur(30px);
          filter: blur(30px);
  box-shadow:
    inset 0 0 0 5px rgba(255,255,255, 0.6),
    inset 100px 100px 0 0px #fa709a,
    inset 200px 200px 0 0px #784ba8,
    inset 300px 300px 0 0px #2b86c5;
}

@-webkit-keyframes move {
  from {
    transform: translate(-100px, -50px) rotate(-90deg);
    border-radius: 24% 76% 35% 65% / 27% 36% 64% 73%;
  }

  to {
    transform: translate(500px, 100px) rotate(-10deg);
    border-radius: 76% 24% 33% 67% / 68% 55% 45% 32%;
  }
}

@keyframes move {
  from {
    transform: translate(-100px, -50px) rotate(-90deg);
    border-radius: 24% 76% 35% 65% / 27% 36% 64% 73%;
  }

  to {
    transform: translate(500px, 100px) rotate(-10deg);
    border-radius: 76% 24% 33% 67% / 68% 55% 45% 32%;
  }
}
</style>
