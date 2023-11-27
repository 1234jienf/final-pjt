<template>
  <div class="main">
    <!-- 은행 필터 -->
    <label for="bankFilter" class="input">은행 선택:</label>
    <select v-model="selectedBank" @change="filterDeposits">
      <option value="">모든 은행</option>
      <option v-for="(bank, id) in bankList" :key="id" :value="id">{{ bank }}</option>
    </select>
    <!-- 저축 기간 필터 -->
    <label for="saveTermFilter">저축 기간 선택:</label>
    <select v-model="selectedSaveTerm" @change="filterDeposits">
      <option value="">모든 저축 기간</option>
      <option v-for="term in saveTerms" :key="term" :value="term">{{ term }}</option>
    </select>
  </div>
  <div class="box" v-if="selectedOptions.length === 0">
    선택한 데이터가 없습니다.
  </div>

  <div class="table-container" v-else>
    <table class="custom-table">
      <thead>
        <tr>
          <th>예금 ID</th>
          <th>은행명</th>
          <th>공시 제출월</th>
          <th>Interest Rate</th>
          <th>Interest Rate 2</th>
          <th>예치 기간</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(seloption, index) in selectedOptions" :key="index" @click="redirectToDetails(seloption)">
          <td>{{ seloption.fin_prdt_cd }}</td>
          <td>{{  bankList[selectedBank] }}</td>
          <td>{{ seloption.dcls_month }}</td>
          <td>{{ seloption.intr_rate }}</td>
          <td>{{ seloption.intr_rate2 }}</td>
          <td>{{ seloption.save_trm }}</td>
        </tr>
      </tbody>
    </table>
  </div>

    <h3>정기예금 목록</h3>
<DepositListItem 
      v-for="option in depositOptions"
      :key="option.id"
      :option="option"
    />
</template>

<script setup>

import { ref, onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';
import DepositListItem from '@/components/DepositListItem.vue'
import axios from 'axios'; // axios import 추가

const selectedBank = ref('');
const selectedSaveTerm = ref('');
const selectedOptions = ref([]);
const store = useCounterStore();
const depositOptions = ref([]);


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

const bank_dir = {
'우리은행': 1,
'한국스탠다드차타드은행': 2,
'대구은행':	3,
'부산은행':	4,
'광주은행':	5,
'제주은행':	6,
'전북은행':	7,
'경남은행':	8,
'중소기업은행':	9,
'한국산업은행':	10,
'국민은행':	11,
'신한은행':	12,
'농협은행주식회사':	13,
'하나은행':	14,
'주식회사 케이뱅크':	15,
'수협은행':	16,
'주식회사 카카오뱅크':	17,
'토스뱅크 주식회사':	18,
}


const banktofin = {
  '우리은행': 'WR0001B',
  '한국스탠다드차타드은행': '00320342',
  '대구은행' : '10511008000996000',
  '부산은행': '01030500510002',

};
const router = useRouter();
const saveTerms = [6, 12, 24, 36];


const fetchData = async () => {
try {
  const data = await store.getDeposit();
  depositOptions.value = data;
} catch (error) {
  console.error(error);
}
};

const filterDeposits = async () => {
  try {
    const bankId = bank_dir[bankList[selectedBank.value]];
    const saveTerm = selectedSaveTerm.value;

    // 선택된 필터가 없을 경우 모든 데이터를 보여줄 수 있도록 수정
    if (!selectedBank.value || !selectedSaveTerm.value) {
      depositOptions.value = await store.getDeposit();
      return;
    }

    const response = await axios.get(`${store.API_URL}/finlife/deposit-sort/${bankId}/${saveTerm}`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });

    // 받은 데이터를 적절히 처리하거나 저장
    if (response.data) {
      selectedOptions.value = response.data;
    } else {
      // 응답이 없을 경우 예외 처리 필요
      console.error('No data found.');
    }
    console.log(selectedOptions.value )
  } catch (error) {
    console.error('Error fetching bank data:', error);
    // 에러 처리
  }
};
const redirectToDetails = async (seloption) => {
  const { fin_prdt_cd, dcls_month, kor_co_nm } = seloption;  
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
onMounted(fetchData);


</script>

<style scoped>
/* 테이블 스타일링 */

.styled-table {
border-collapse: collapse;
margin: 25px 0;
font-size: 0.9em;
font-family: sans-serif;
min-width: 400px;
box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.styled-table thead th {
padding: 12px 15px;
text-align: left;
font-weight: bold;
border-bottom: 1px solid #ddd;
}

.styled-table tbody td {
padding: 12px 15px;
text-align: right;
vertical-align: top;
}

.styled-table tbody tr {
border-bottom: 1px solid #ddd;
}

.styled-table tbody tr:last-of-type {
border-bottom: 2px solid #009879;
}

/* 스크롤 가능한 테이블 스타일 */
.scroll-table {
max-height: 500px; /* 원하는 높이 설정 */
overflow-y: auto;
}

.main {
  border: none;
  text-align: center;
  color: black;
  background-color: white;
  cursor: pointer;
  font-family: 'SpoqaHanSansNeo-Regular', sans-serif;
  font-size: large;
}

h1{
  text-align: center;
  justify-content: center;
}

.box {
  /* 크기와 스타일 조정 */
  margin: 20px;
  padding: 20px;
  height: 100px;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  border-radius: 8px;
  color: #333;
}

.table-container {
  margin: 20px;
}

.custom-table {
  /* 테이블 스타일 조정 */
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  font-family: 'SpoqaHanSansNeo-Bold', sans-serif;
  border: 1px solid #ddd;
}

.custom-table th,
.custom-table td {
  /* 테이블 셀 스타일 */
  padding: 8px;
  border: 1px solid #ddd;
}

.custom-table th {
  /* 테이블 헤더 스타일 */
  background-color: #f2f2f2;
  font-weight: bold;
  text-align: left;
}

.custom-table tbody tr:hover {
  /* 마우스 호버 시 배경색 변경 */
  background-color: #f9f9f9;
  cursor: pointer;
}

select {
  border: none;
  text-align: center;
  color: black;
  background-color: white;
  padding: 0.1rem 1rem;
  border-radius: 0.2rem;
  cursor: pointer;
  font-family: 'SpoqaHanSansNeo-Regular', sans-serif;
  font-size: large;
}


</style>
