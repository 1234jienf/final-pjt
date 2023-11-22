<template>
  <div class="detail">
    <div class="card" v-if="depositDetail">
      <h1 class="card-title">{{ depositDetail.fin_prdt_cd }} 상품</h1>
      <div class="detail-info">
        <p><strong>Deposit ID: </strong>{{ depositDetail.id }}</p>
        <p><strong>fin_prdt_cd: </strong>{{ depositDetail.fin_prdt_cd }}</p>
        <p><strong>공시 제출월: </strong> {{ depositDetail.dcls_month }}</p>
        <p><strong>금융회사명: </strong> {{ depositDetail.kor_co_nm }}</p>
        <p><strong>상품명: </strong>{{ depositDetail.fin_prdt_nm }}</p>
        <p><strong>가입제한: </strong>{{ depositDetail.join_deny }}</p>
        <p><strong>가입방법: </strong>{{ depositDetail.join_way }}</p>
        <p><strong>우대조건: </strong>{{ depositDetail.spcl_cnd }}</p>
      </div>
      <div>
        현재 가입중인 상품:
        {{ store.userInfo.financial_products }}
      </div>
      <button v-if="isJoined" class="join-button" @click="handleJoinButtonClick">가입해지</button>
      <button v-else class="join-button" @click="handleJoinButtonClick">가입하기</button>    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted,computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router';

const store = useCounterStore();
const depositDetail = ref(null);
const route = useRoute()


const getUserProductIds = () => {
  const products = store.userInfo.financial_products || '';
  console.log(products)
  return products.split(',').map(id => id.trim());
};

// 해당 상품이 이미 가입되어 있는지 확인하는 함수
const isProductAlreadyJoined = (productId) => {
  const joinedProducts = getUserProductIds();
  return joinedProducts.includes(productId);
};


const handleJoinButtonClick = (productId) => {
  if (isProductAlreadyJoined(productId)) {
    // 이미 가입되어 있는 상품이라면 해지 로직 실행
    const updatedProducts = getUserProductIds().filter(id => id !== productId).join(',');
    store.updateUserInfo('financial_products', updatedProducts);
    console.log('해당 상품 해지:', productId);
    // 필요한 처리 또는 UI 변경
  } else {
    // 가입 로직 실행
    const updatedProducts = (store.userInfo.financial_products || '') + ',' + productId;
    store.updateUserInfo('financial_products', updatedProducts);
    console.log('해당 상품 가입:', productId);
    // 필요한 처리 또는 UI 변경
  }
};

// 가입 버튼 클릭 이벤트에 handleJoinButtonClick 함수 연결
const joinDeposit = () => {
  const productId = route.params.fin_prdt_cd;
  handleJoinButtonClick(productId);
};

// 기존의 fetchDepositDetail 함수에서 joinDeposit를 호출하는 부분을 수정
const fetchDepositDetail = async () => {
  const productId = route.params.fin_prdt_cd;
  
  try {
    const response = await axios.get(`${store.API_URL}/finlife/deposit-detail/${productId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    depositDetail.value = response.data;
    joinDeposit(); // 상품 상세 정보를 받아온 후에 가입 버튼 동작 수행
  } catch (error) {
    console.error('Error fetching deposit details:', error);
  }
};

const isJoined = computed(() => {
  const productId = route.params.fin_prdt_cd;
  return isProductAlreadyJoined(productId);
});

onMounted(() => {
  fetchDepositDetail();
});

console.log(store.userInfo.financial_products)
</script>

<style scoped>
.detail {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.card {
  background-color: #EAEFFE;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.card-title {
  color: #526ADF;
  margin-bottom: 15px;
}

.detail-info {
  background-color: #ffffff;
  padding: 15px;
  border-radius: 5px;
  margin-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.detail-info p {
  margin-bottom: 8px;
}

.join-button {
  /* 버튼 스타일 */
  background-color: #526ADF;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.join-button:hover {
  background-color: #4054b2;
}
</style>
