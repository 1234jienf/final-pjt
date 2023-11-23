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
    <div v-if="mbti" class="recommended-products">
      <h1>{{ mbti }} 가 택한 TOP10 상품</h1>
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
    <div v-else>
      <!-- <RouterLink :to="{ name: 'SurveyView' }">MBTI 검사하러가기</RouterLink> -->
    </div>
  </template>
  
<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
  
const mbti = ref('')
const recommended_products = ref([])
const companies = ref([])
const pd_names = ref([])
const store = useCounterStore()
const router = useRouter()

onMounted(async () => {
    await store.getmbtiRecommended();
    mbti.value = store.mbtiData.mbti
    recommended_products.value = store.mbtiData.recommended_products
    companies.value = store.mbtiData.companies
    pd_names.value = store.mbtiData.pd_names
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
    
    
  }</style>
  