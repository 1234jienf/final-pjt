<template>
  <div class="body">
    <div v-if="loading">
      <!-- 로딩 중일 때 보여줄 화면 -->
      <div class="loader">
        <div class="loading">LOADING</div>
        <div v-for="(_, i) in Array.from({ length: 8 })" :key="i" :style="{ '--i': i }" class="loader-circle"></div>
      </div>
    </div>
    <div v-else>
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
  </div>
  
  <div class="recommended-products">
      <h1>추천 상품</h1>
      <div class="card-container">
        <div
          v-for="(company, index) in companies"
          :key="index"
          class="card"
          @click="redirectToDetail(index)"
        >{{ index +1 }}
        <p>{{ company }} - {{ pd_names[index] }}</p>
        </div>    
    </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useCounterStore()
const recommended_products = ref([])
const companies = ref([])
const router = useRouter()
const pd_names = ref([])
const loading = ref(true); // 초기 로딩 상태를 true로 설정


onMounted(async () => {
  await store.getRecommendedProducts();
  recommended_products.value = store.recommendedData.recommended_products
  companies.value = store.recommendedData.companies
  pd_names.value = store.recommendedData.pd_names
  loading.value = false; // 데이터 로딩이 완료되면 로딩 상태를 false로 변경
});

const redirectToDetail = async (index) => {
  const productId = recommended_products.value[index];
  
  try {
    // 여기서 productId를 이용하여 요청을 보내고, 해당하는 뷰로 라우팅합니다.
    // 예시로 deposit detail로 라우팅하는 것을 보여드리겠습니다.
    const response = await axios.get(`${store.API_URL}/finlife/deposit-detail/${productId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    
    // 라우팅
    await router.push({
      name: 'DepositDetailView',
      params: {
        fin_prdt_cd: productId
      }
    });
  } catch (error) {
  try {
    const response = await axios.get(`${store.API_URL}/finlife/saving-detail/${productId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    await router.push({
      name: 'SavingDetailView',
      params: {
        fin_prdt_cd: productId
      }
    });
   
  } catch (error) {
    console.error('Error fetching savings:', error);
  }
};
}
</script>

<style scoped>

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
  justify-content: center;
}

.card {
  width: 200px;
  height: 100px;
  padding: 10px;
  background-color: #ffffff;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}

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
  
}


.loader {
  background: #EAEFFE;
  height: 100vh;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loader::before {
  background: linear-gradient(to right, #917173, #2a3b36, #432c52);
  content: "";
  background: rgba(255, 255, 255, 0);
  backdrop-filter: blur(0.3px);
  position: absolute;
  width: 140px;
  height: 55px;
  z-index: 20;
  border-radius: 0 0 10px 10px;
  border: 1px solid rgba(255, 255, 255, 0.274);
  border-top: none;
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.082);
  flex-direction: column; /* 컨텐츠를 세로로 배치하기 위해 컬럼 방향 설정 */

  animation: anim2 2s infinite;
}


.loading {
  position: relative;
  background: #EAEFFE;
  margin-bottom: 20px; /* loader와의 간격 조정 */

}

@keyframes anim {
  0%,
  100% {
    transform: translateY(5px);
  }
  50% {
    transform: translateY(-65px);
  }
}

@keyframes anim2 {
  0%,
  100% {
    transform: rotate(-10deg);
  }
  50% {
    transform: rotate(10deg);
  }
}

</style>
