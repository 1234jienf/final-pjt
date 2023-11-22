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
      <button class="join-button" @click="joinDeposit">가입하기</button>
    </div>
  </div>
</template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRoute } from 'vue-router';
  
  const store = useCounterStore();
  const savingDetail = ref(null);
  const route = useRoute()
  
  const fetchSavingDetail = async () => {
    const savingId = route.params.fin_prdt_cd;
    console.log(savingId);
    
    try {
      const response = await axios.get(`${store.API_URL}/finlife/saving-detail/${savingId}/`, {
        headers: {
          Authorization: `Token ${store.token}`
        }
      });
      savingDetail.value = response.data;
    } catch (error) {
      console.error('Error fetching saving details:', error);
    }
  };

  const joinDeposit = () => {
  // 여기서 가입 폼을 처리하는 로직을 추가하세요.
  // 예시: 가입 폼을 모달이나 새 창으로 띄우거나, 라우터를 통해 다른 페이지로 이동하는 등의 동작을 수행합니다.
  console.log('가입하기 버튼을 클릭했습니다.');
};
  
  onMounted(() => {
    fetchSavingDetail();
  });
  

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
  