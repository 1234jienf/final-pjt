<template>
  <div class="container">
    <div class="sidebar" :style="{ backgroundColor: '#EAEFFE', color: '#526ADF' }">
      <nav>
        <div class="box-container">
          <div class="box">
            <RouterLink :to="{ name: 'ProfileView' }">기본 정보 수정</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'RecommendedProductsView' }">상품 추천받기</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'MbtiRecommendView' }">MBTI별 추천 상품</RouterLink>
          </div>
        </div>
      </nav>
    </div>
  </div>
  <div class="recommended-products">
    <h1>추천 상품</h1>
    <ol>
      <li v-for="i in companies.length">{{ companies[i-1] }} - {{ pd_names[i-1] }}</li>
    </ol>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';

const store = useCounterStore()
const recommended_products = ref([])
const companies = ref([])
const pd_names = ref([])


onMounted(async () => {
  await store.getRecommendedProducts();
  recommended_products.value = store.recommendedData.recommended_products
  companies.value = store.recommendedData.companies
  pd_names.value = store.recommendedData.pd_names
});
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
  
}</style>
