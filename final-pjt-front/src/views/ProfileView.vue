<template>
  <div class="container">
    <div class="sidebar" :style="{ backgroundColor: '#EAEFFE', color: '#526ADF' }">
      <nav>
        <div class="box-container">
          <div class="box">
            <RouterLink :to="{ name: 'ProfileView' }" class="text-dec">기본 정보 수정</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'RecommendedProductsView' }" class="text-dec">상품 추천받기</RouterLink>
          </div>
          <div class="box">
            <RouterLink :to="{ name: 'MbtiRecommendView' }" class="text-dec">MBTI별 추천 상품</RouterLink>
          </div>
        </div>
      </nav>
    </div>
  </div>
  <div class="mdl">
  <div class="circles">
    <div class="circle circle-1"></div>
    <div class="circle circle-2"></div>
  </div>  
</div>
<div class="profile">
  <div class="card">
  <h1>프로필</h1>
  <div class="profile-info">
    <p>회원번호 : {{ store.userInfo.id }}</p>
    <p>아이디 : {{ store.userInfo.username }}</p>
    <p class="edit-number">
      이메일 :
      <span v-if="editingField === 'email'">
        <input v-model="editValues.email" />
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        <span v-if="store.userInfo.email">{{ store.userInfo.email }}</span>
        <span v-else>이메일을 입력하세요</span>
        <button @click="editField('email')" class="btn">수정</button>
      </span>
    </p>
    <p>
      닉네임 :
      <span v-if="editingField === 'nickname'">
        <input v-model="editValues.nickname" />
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        <span v-if="store.userInfo.nickname">{{ store.userInfo.nickname }}</span>
        <span v-else> 없음 </span>
        <button @click="editField('nickname')" class="btn">수정</button>
      </span>
    </p>
    <p>
      나이 :
      <span v-if="editingField === 'age'">
        <input v-model="editValues.age" type="number" />
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        {{ store.userInfo.age }}
        <button @click="editField('age')" class="btn">수정</button>
      </span>
    </p>
    <p>
      현재 가진 금액 :
      <span v-if="editingField === 'money'">
        <input v-model="editValues.money" type="number" />
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        {{ store.userInfo.money }}
        <button @click="editField('money')" class="btn">수정</button>
      </span>
    </p>
    <p>
      연봉 :
      <span v-if="editingField === 'salary'">
        <input v-model="editValues.salary" type="number" />
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        {{ store.userInfo.salary }}
        <button @click="editField('salary')" class="btn">수정</button>
      </span>
    </p>
    <p>
      mbti :
      <span v-if="editingField === 'mbti'">
        <input v-model="editValues.mbti"/>
        <button @click="submitChanges" class="btn">저장</button>
      </span>
      <span v-else>
        {{ store.userInfo.mbti }}
        <button @click="editField('mbti')" class="btn">수정</button>
      </span>
    </p>
  </div>
</div>
  <br>
  <div class="chart-container">
    <h2>가입한 상품 금리</h2>
    <canvas id="myChart"></canvas>
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
salary: 0,
mbti: ''
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
margin-bottom: 20px;

}
.card{
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(35px);
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 80px rgba(0, 0, 0, 0.25);
  padding: 30px 30px 30px 30px;
  overflow: hidden;
  
}
.profile h1 {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  font-family: 'SpoqaHanSansNeo-Bold', sans-serif;

}

.profile-info p {
margin-bottom: 8px;
font-family: 'SpoqaHanSansNeo-Thin', sans-serif;
font-size: large;

}
.edit-number {
   position:relative; 
   display: inline-block;
    overflow: hidden;
    margin-bottom:30px; 
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
.text-dec{
  text-decoration: none;
  color: black; /* 글자색 변경 */
  font-family: 'SpoqaHanSansNeo-Regular', sans-serif;
  font-size: large;
}
.container {
display: flex; /* 주어진 색상 적용 */
border-radius: 10px;
overflow: hidden;

box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2); /* 적당한 그림자 추가 */
}

.box:hover {
  box-shadow: -2px -2px 5px #FFF,  5px #BABECC;
  transform: scale(1.05); /* 확대 효과 */
  
}
input{
  border: none;
  text-align: center;
  color: black;
  background-color: white;
  padding: 0.1rem 1rem;
  border-radius: 0.2rem;
  cursor: pointer;
  font-family: 'SpoqaHanSansNeo-Thin', sans-serif;
  font-size: large;
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

.btn {
  background: none;
  border: none;
  text-align: center;
  font-size: 1rem;
  color: whitesmoke;
  background-color: #1f1f47;
  padding: 0.1rem 0.5rem;
  border-radius: 0.2rem;
  cursor: pointer;
  font-family: 'SpoqaHanSansNeo-Thin', sans-serif;
  font-size: large;
}

body{
  display: block;
  position: center;
    font-family: 'Space Mono', monospace;
    background-color: rgb(240, 244, 247);
  background: linear-gradient(-70deg,  #202020, #000000);
  height: 100vh;
  
}




/* Background circles start */
.circle {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(120deg, rgb(82, 106, 223), #2c3e50);
}
.circles {
  position: absolute;
  height: 270px;
  width: 450px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: -1;
}
.circle-1 {
  height: 300px;
  width: 300px;
  top: 100px;
  left: -50px;
  opacity: 0.8;
  animation-timing-function: cubic-bezier(0.54, 0.085, 0.5, 0.92);
  animation-iteration-count: infinite;
  animation-name: float;
  -webkit-animation-name: float;
  animation-duration: 6s;
  -webkit-animation-duration: 6s;
  -webkit-animation-delay: 3.5s;
  animation-delay: 3.5s;
  animation-direction: alternate;
  
}

.circle-2 {
  height: 240px;
  width: 240px;
  bottom: 40px;
  right: -100px;
  opacity: 0.8;
  animation-timing-function: cubic-bezier(0.54, 0.085, 0.5, 0.92);
  animation-iteration-count: infinite;
  animation-name: float;
  -webkit-animation-name: float;
  animation-duration: 6s;
  -webkit-animation-duration: 6s;
  -webkit-animation-delay: 2s;
  animation-delay: 2s;
  animation-direction: alternate;
}
/* Background circles end */





/* ANIMATIONS */
@keyframes explode {
 0% { opacity: 1; }
 100% { transform: scale(1.2); opacity: 0; }
}
@keyframes float {

  0% {
    -webkit-transform: rotateX(0deg) translateY(0px);
    -moz-transform: rotateX(0deg) translateY(0px);
    -ms-transform: rotateX(0deg) translateY(0px);
    -o-transform: rotateX(0deg) translateY(0px);
    transform: rotateX(0deg) translateY(0px);
    }

  50% {
    -webkit-transform: rotateX(0deg) translateY(1px) translateX(5px);
    -moz-transform: rotateX(0deg) translateY(10px) translateX(5px);
    -ms-transform: rotateX(0deg) translateY(30px) translateX(5px);
    -o-transform: rotateX(0deg) translateY(40px) translateX(5px);
    transform: rotateX(0deg) translateY(10px) translateX(5px);
}
  100% {
    -webkit-transform: rotateX(0deg) translateY(0px) translateX(1px);
    -moz-transform: rotateX(0deg) translateY(0px) translateX(1px);
    -ms-transform: rotateX(0deg) translateY(0px) translateX(1px);
    -o-transform: rotateX(0deg) translateY(0px) translateX(1px);
    transform: rotateX(0deg) translateY(0px) translateX(1px);
  }

}

.mdl{
  height: auto;
  width: 420px;
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-60%,-60%);

}
</style>