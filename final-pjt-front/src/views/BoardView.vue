<template>
  <div class="container">
  <div class="sidebar" :style="{ backgroundColor: '#EAEFFE', color: '#526ADF' }">
    <nav>
      <div class="box-container">
        <div class="box">
          <a href="" class="text-dec">전체 글 보기</a>
        </div>
        <div class="box">
          <RouterLink :to="{ name: 'CreateView' }" class="text-dec ">
      글 작성하기
    </RouterLink>
          
        </div>
      </div>

      </nav>
  </div>

  
  <div class="board-page">
    <h1>커뮤니티</h1>
    <BoardList />
  </div>
</div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/BoardList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getBoards()
})
</script>

<style scoped>
/* Board Page 스타일 */

.container {
  display: flex; /* 주어진 색상 적용 */
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2); /* 적당한 그림자 추가 */
}

.sidebar {
  flex: 1;
  border-right: 1px solid #c2dfff; /* 투명한 테두리 */
  padding: 20px;
  height: 100vh;

}
.board-page {
  margin: 20px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  width: 70%; 
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(35px);
  padding: 30px 30px 30px 30px;
  overflow: hidden;
  
}

.create-link {
  border: none;
  outline: none;
  font-size: 16px;
  border-radius: 20px;
  padding: 16px;
  background-color: #EBECF0;
  text-shadow: 1px 1px 0 #FFF;
  cursor: pointer;
  font-weight: 600;
  box-shadow: -5px -5px 20px #FFF, 5px 5px 20px #BABECC;
  transition: all 0.2s ease-in-out;
}

.create-link:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
}

.create-link:active {
  box-shadow: inset 1px 1px 2px #c2dfff, inset -1px -1px 2px #FFF;
}
.a{
  
}

label {
  display: block;
  margin-bottom: 24px;
  width: 100%;
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
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    border-radius: 1px; /* 원하는 값으로 조정 */
    transition: all 0.2s ease-in-out;
  }
.box:hover {
  box-shadow: -2px -2px 5px #FFF,  5px #BABECC;
  transform: scale(1.05); /* 확대 효과 */
}

.main-content {
  flex: 4;
  padding: 20px;
}
.text-dec{
  text-decoration: none;
  color: #526ADF; /* 글자색 변경 */
  font-family: 'SpoqaHanSansNeo-Regular', sans-serif;
  font-size: large;
}

</style>
