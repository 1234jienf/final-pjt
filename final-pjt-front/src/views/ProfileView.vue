<template>
  <div class="profile">
    <h1>프로필</h1>
    <div class="profile-info">
      <p>회원번호 : {{ store.userInfo.id }}</p>
      <p>아이디 : {{ store.userInfo.username }}</p>
      <p>
        이메일 :
        <span v-if="editingField === 'email'">
          <input v-model="editValues.email" />
          <button @click="submitChanges">저장</button>
        </span>
        <span v-else>
          <span v-if="store.userInfo.email">{{ store.userInfo.email }}</span>
          <span v-else>이메일을 입력하세요</span>
          <button @click="editField('email')">수정</button>
        </span>
      </p>
      <p>
        닉네임 :
        <span v-if="editingField === 'nickname'">
          <input v-model="editValues.nickname" />
          <button @click="submitChanges">저장</button>
        </span>
        <span v-else>
          <span v-if="store.userInfo.nickname">{{ store.userInfo.nickname }}</span>
          <span v-else>없음</span>
          <button @click="editField('nickname')">수정</button>
        </span>
      </p>
      <p>
        나이 :
        <span v-if="editingField === 'age'">
          <input v-model="editValues.age" type="number" />
          <button @click="submitChanges">저장</button>
        </span>
        <span v-else>
          {{ store.userInfo.age }}
          <button @click="editField('age')">수정</button>
        </span>
      </p>
      <p>
        현재 가진 금액 :
        <span v-if="editingField === 'money'">
          <input v-model="editValues.money" type="number" />
          <button @click="submitChanges">저장</button>
        </span>
        <span v-else>
          {{ store.userInfo.money }}
          <button @click="editField('money')">수정</button>
        </span>
      </p>
      <p>
        연봉 :
        <span v-if="editingField === 'salary'">
          <input v-model="editValues.salary" type="number" />
          <button @click="submitChanges">저장</button>
        </span>
        <span v-else>
          {{ store.userInfo.salary }}
          <button @click="editField('salary')">수정</button>
        </span>
      </p>
    </div>
    <br>
    <div class="chart-container">
      <h2>가입한 상품 금리</h2>
      <canvas id="myChart"></canvas>
    </div>
    <div>
      <router-link to="/recommended-products">추천 상품 보러 가기</router-link>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';
import Chart from 'chart.js/auto';



const store = useCounterStore();
const editingField = ref([null])
const editValues = ref({
  email: '',
  nickname: '',
  age: 0,
  money: 0,
  salary: 0
})

function editField(field) {
  editingField.value = field
  editValues.value[field] = store.userInfo[field]
}

function submitChanges() {
  const field = editingField.value;

  if (field) {
    store.updateUserInfo(field, editValues.value[field]); // 수정: editValues
    editingField.value = null;
  }
}

onMounted(async () => {
  try {
    await store.getUserInfo();
    await store.getUserChart();

    if (!store.isLoading) {
      drawChart();
    }
  } catch (error) {
    console.error(error);
  }
});

// 차트를 그리는 함수
async function drawChart() {
  const chartData = store.userProduct;

  if (!chartData.fin_prdt_nms || chartData.fin_prdt_nms.length === 0) {
    console.warn('Data not loaded. Cannot draw chart.');
    return;
  }
  // 차트를 그릴 canvas 요소를 선택
  const canvas = document.getElementById('myChart');

  if (canvas) {
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
  }

  if (canvas) {
    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['평균', ...chartData.fin_prdt_nms],
        datasets: [
          {
            label: '저축금리',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: [chartData.average_saving_rate, ...chartData.saving_rates],
          },
          {
            label: '우대금리',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            data: [chartData.average_max_rate, ...chartData.max_rates],
          },
        ],
      },
    });
  }
}
</script>

<style scoped>
.profile {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  margin-bottom: 20px;
}

.profile h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

.profile-info p {
  margin-bottom: 8px;
}

.profile-info p:last-child {
  margin-bottom: 0;
}

.profile-info p span {
  font-weight: bold;
}

.profile-info p span:last-child {
  font-weight: normal;
}
</style>