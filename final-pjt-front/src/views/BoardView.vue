<template>
  <div class="container">
  <aside class="sidebar">
    <nav class="nav">
      <ul>
        <li class="active"><a href="#">전체 글 보기</a></li>
        <li><a href="#">내 글 보기</a></li>
      </ul>
    </nav>
  </aside>
  <div class="board-page">
    <h1>커뮤니티</h1>
    <label>
    <RouterLink :to="{ name: 'CreateView' }" class="create-link ">
      글 작성하기
    </RouterLink>
  </label>
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
  display: flex;
}
.board-page {
  margin: 20px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  width: 70%; 
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


label {
  display: block;
  margin-bottom: 24px;
  width: 100%;
}

.sidebar {
  width: 15%;
  height: 100vh;
  background: #c2dfff;;
  font-size: 0.65em;
  
}

.nav {
  position: relative;
  margin: 0 15%;
  text-align: right;
  top: 50%;
  transform: translateY(-50%);
  font-weight: bold;
}
.container {
  display: flex;
  justify-content: space-between;
}

.sidebar {
  width: 25%;
  height: 100vh;
}

.nav ul {
  list-style: none;
}
.nav ul li {
    position: relative;
}
.nav ul li a {
      line-height: 10em;
      display: block;
    }
.nav ul li a:active a {
      color: rgb(121, 51, 51);
}
    
  

</style>
