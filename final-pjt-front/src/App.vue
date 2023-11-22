<template>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" />
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />
<link href="https://cdn.jsdelivr.net/gh/toss/tossface/dist/tossface.css" rel="stylesheet" type="text/css" />
  <header class="navbar">
    <div class="label-wrapper">
      <div class="menu-toggle" @click="toggleDropdown">
        <font-awesome-icon :icon="['fas', 'bars']" size="lg" style="color: #526ADF;" />
      </div>
    </div>
    <div class="user-actions" v-show="store.isLogin">
      <RouterLink :to="{ name: 'ProfileView' }" class="profile-link">
        <font-awesome-icon :icon="['fas', 'user']" size="2xl" style="color: #526ADF;" />
      </RouterLink>
      <form @submit.prevent="store.logOut" class="profile-link">
        <button type="submit" class="logout-btn">
          <font-awesome-icon :icon="['fas', 'arrow-right-from-bracket']" size="2xl" />
        </button>
      </form>
    </div>
    <div class="user-actions" v-show="!store.isLogin">
      <RouterLink :to="{ name: 'SignUpView' }" class="btn-2">
        <font-awesome-icon :icon="['fas', 'user-plus']" />
      </RouterLink>
      <RouterLink :to="{ name: 'LogInView' }" class="btn-2">
        <div class="box">Login</div>
      </RouterLink>
    </div>
    <nav class="dropdown" :class="{ active: showDropdown }">
      <RouterLink :to="{ name: 'MainPageView' }" class="nav-link btn-2">홈</RouterLink>
      <RouterLink :to="{ name: 'DepositView' }" class="nav-link btn-2">정기 예금/적금</RouterLink>
      <RouterLink :to="{ name: 'CalculatorView' }" class="nav-link btn-2">환율 계산기</RouterLink>
      <RouterLink :to="{ name: 'KakaomapView' }" class="nav-link btn-2">지도보기</RouterLink>
      <RouterLink :to="{ name: 'BoardView' }" class="nav-link btn-2">커뮤니티</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>


<script setup>
import { ref } from 'vue';
import { RouterView, RouterLink } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const showDropdown = ref(false);

const dropdownTop = ref(0);
const dropdownLeft = ref(0);
const toggleDropdown = () => {
  showDropdown.value = !showDropdown.value;
};

window.addEventListener('click', (e) => {
  if (!e.target.closest('.menu-toggle')) {
    showDropdown.value = false;
  }
});

</script>

<style scoped>

.navbar {
  justify-content: space-between;
  background-color: #EAEFFE;
  justify-content: center;
  align-items: center;
}


.user-actions {
  display: flex;
  flex-direction: row-reverse;
  align-items: center;
  gap: 3px; /* 간격 추가 */
}

/* Dropdown styles */
.dropdown {
  background-color: #EAEFFE;
  min-width: 160px;
  display: none; /* Initially hide the dropdown */
  transition: opacity 0.5s ease; /* 투명도 변화에 대한 transition 추가 */
  opacity: 0; /* 처음에는 숨겨진 상태로 설정 */
  pointer-events: none; /* 숨겨진 상태에서 이벤트 비활성화 */
  font-weight: bold;

}

.dropdown.active {
  display: block; /* Show the dropdown when active class is applied */
  opacity: 5; /* 활성화될 때 투명도 증가 */
  pointer-events: auto; /* 활성화될 때 이벤트 활성화 */
}
.dropdown a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: center; 
  cursor: pointer;
}

.dropdown a:hover {
  border-radius: 10px; /* hover 시 둥글게 조정되도록 설정 */
  transform: scale(1.1); /* 확대 효과 */
  color: black; /* 글자색 변경 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* 그림자 효과 */
}

.label-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 24px; /* Adjust the font size to your desired larger size */
}
.logout-btn {
  border: none;
  background: none;
  cursor: pointer;
  padding: 0;
  font-size: 16px;
  color: #526ADF;
  margin: 0;
}

.profile-link {
  margin-right: 10px; /* 로그아웃과 프로필 링크 사이의 간격을 줍니다. */
}

.box {
    width: 50px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border-radius: 5px; /* 원하는 값으로 조정 */
    color: #526ADF;
  }
  template {
    font-family: 'Tossface';
  }

</style>