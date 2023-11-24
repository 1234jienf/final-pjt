<template>
  <div class="detail">
    <div class="card" v-if="savingDetail">
      <h1 class="card-title">{{ savingDetail.fin_prdt_cd }} 상품</h1>
      <div class="detail-info">
        <p><strong>Saving ID: </strong>{{ savingDetail.id }}</p>
        <p><strong>fin_prdt_cd: </strong>{{ savingDetail.fin_prdt_cd }}</p>
        <p><strong>공시 제출월: </strong> {{ savingDetail.dcls_month }}</p>
        <p><strong>금융회사명: </strong> {{ savingDetail.kor_co_nm }}</p>
        <p><strong>상품명: </strong>{{ savingDetail.fin_prdt_nm }}</p>
        <p><strong>가입제한: </strong>{{ savingDetail.join_deny }}</p>
        <p><strong>가입방법: </strong>{{ savingDetail.join_way }}</p>
        <p><strong>우대조건: </strong>{{ savingDetail.spcl_cnd }}</p>
      </div>
      <button v-if="isJoined" class="join-button" @click="joinSaving()">가입해지</button>
      <button v-else class="join-button" @click="joinSaving()">가입하기</button>    
    </div>
    </div>

</template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted,computed } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRoute } from 'vue-router';
  
  const store = useCounterStore();
  const savingDetail = ref(null);
  const route = useRoute()
  

  const getUserProductIds = () => {
  return (store.userInfo.financial_products || '').split(',').map(id => id.trim());
};

const isProductAlreadyJoined = (productId) => {
  const joinedProducts = getUserProductIds();
  return joinedProducts.includes(productId);
};


const handleJoinButtonClick = (productId) => {
  if (!isProductAlreadyJoined(productId)) {
    const updatedProducts = `${store.userInfo.financial_products || ''},${productId}`;
    store.updateUserInfo('financial_products', updatedProducts);
    console.log('해당 상품 가입:', productId);
  } else {
    const updatedProducts = getUserProductIds().filter(id => id !== productId).join(',');
    store.updateUserInfo('financial_products', updatedProducts);
    console.log('해당 상품 해지:', productId);
  }
};

const joinSaving = () => {
  const productId = route.params.fin_prdt_cd;
  handleJoinButtonClick(productId);
};

const fetchSavingDetail = async () => {
  const productId = route.params.fin_prdt_cd;
  
  try {
    const response = await axios.get(`${store.API_URL}/finlife/saving-detail/${productId}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    savingDetail.value = response.data;
  } catch (error) {
    console.error('Error fetching saving details:', error);
  }
};

const isJoined = computed(() => {
  const productId = route.params.fin_prdt_cd;
  return isProductAlreadyJoined(productId);
});

onMounted(() => {
  fetchSavingDetail();
});

console.log(store.userInfo.financial_products)

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
  