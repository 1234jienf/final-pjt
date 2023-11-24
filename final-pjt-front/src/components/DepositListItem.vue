<template>
  <div>
  <div class="table-container">
    <table class="custom-table">
      <thead>
        <tr>
          <th>예금 ID</th>
          <th>은행명</th>
          <th>상품명</th>
          <th>공시 제출월</th>
          <th>Interest Rate</th>
          <th>Interest Rate 2</th>
          <th>예치 기간</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(deposit, index) in deposits" :key="index" @click="redirectToDetails(deposit)">
          <td>{{ deposit.fin_prdt_cd }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td>{{ option.dcls_month }}</td>
          <td>{{ option.intr_rate }}</td>
          <td>{{ option.intr_rate2 }}</td>
          <td>{{ option.save_trm }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  
</div>

</template>
  
<script setup>
import { useCounterStore } from '../stores/counter';
import axios from 'axios';
import { ref, onMounted,computed  } from 'vue';
import { defineProps } from 'vue';
import { useRouter } from 'vue-router';

  
const store = useCounterStore();
const deposits = ref([]);
const props = defineProps({
  option: Object
});
  


const bankList = {
  1: '우리은행',
  2: '한국스탠다드차타드은행',
  3: '대구은행',
  4: '부산은행',
  5: '광주은행',
  6: '제주은행',
  7: '전북은행',
  8: '경남은행',
  9: '중소기업은행',
  10: '한국산업은행',
  11: '국민은행',
  12: '신한은행',
  13: '농협은행주식회사',
  14: '하나은행',
  15: '주식회사 케이뱅크',
  16: '수협은행',
  17: '주식회사 카카오뱅크',
  18: '토스뱅크 주식회사'
};


const router = useRouter();
const saveTerms = [6, 12, 24, 36];

const fetchDeposits = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/finlife/deposit-detail/${props.option.fin_prdt_cd}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    deposits.value = Array.isArray(response.data) ? response.data : [response.data];
  } catch (error) {
    console.error('Error fetching deposits:', error);
  }
};

// const DepositSort = function () {
//   // console.log(props.option)
//     axios({
//       method: 'get',
//       url: `${API_URL}/finlife/deposit-sort/${deposit.id}`,
//       headers: {
//         Authorization:`Token ${token.value}`
//       }
//     })
//       .then((res) =>{
//         // console.log(res)
//         boards.value = res.data
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//   }



const redirectToDetails = async (deposit) => {
  const { fin_prdt_cd, dcls_month, kor_co_nm } = deposit;  
  console.log(fin_prdt_cd)
  try {
  await router.push({
    name: 'DepositDetailView',
     // DepositDetailView의 이름
    params: {
      fin_prdt_cd: fin_prdt_cd
    }
  });
} catch (error) {
  console.error('Error redirecting to details:', error);
}
};
  
onMounted(() => {
  // DepositSort();
  fetchDeposits();
});
</script>

<style>
.table-container {
  margin-top: 20px;
}

.custom-table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background-color: #f5f5f5;
}

th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tbody tr:hover {
  background-color: #f9f9f9;
  cursor: pointer;
}  </style>
  