<template>
  <div class="container">
    <div class="sidebar" :style="{ backgroundColor: '#EAEFFE', color: '#526ADF' }">
      <nav>
        <div class="box-container">
          <div class="box">
            <RouterLink :to="{ name: 'DepositView' }">Deposit View</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'SavingView' }">Saving View</RouterLink>
          </div>
        </div>
      </nav>
    </div>
    <div class="main-content">
      <h1>정기 적금 검색하기</h1>
      <SavingList />
    </div>
  </div>
</template>

<script setup>
import SavingList from '@/components/SavingList.vue'
import { RouterView, RouterLink } from 'vue-router';
</script>

<style scoped>
.container {
  display: flex; /* 주어진 색상 적용 */
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2); /* 적당한 그림자 추가 */
}

.sidebar {
  flex: 1;
  border-right: 1px solid #c2dfff; /* 투명한 테두리 */
  padding: 20px;
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
    height: 50px;
    background-color: #EAEFFE;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border-radius: 1px; /* 원하는 값으로 조정 */
    color: #c2dfff;
    transition: all 0.2s ease-in-out;
  }
.box:hover {
  box-shadow: -2px -2px 5px #FFF,  5px #BABECC;
  transform: scale(1.05); /* 확대 효과 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* 그림자 효과 */
}

.main-content {
  flex: 4;
  padding: 20px;
}
</style>
