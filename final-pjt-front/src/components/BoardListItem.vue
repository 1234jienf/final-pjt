<template>
  <div class="board-item">
    <h5 class="board-id">{{ board.id }}</h5>
    <p class="board-title">{{ board.title }}</p>
    <p class="board-content">{{ board.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: board.id }}" class="detail-link">
      자세히 보기
    </RouterLink>
    <hr>
  </div>
</template>
  
<script setup>
import { RouterLink } from 'vue-router'
  
defineProps({
  board: Object
})
</script>

<style scoped>
/* Board Item 스타일 */
.board-item {
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.board-id {
  margin-bottom: 5px;
  color: #777;
}

.board-title {
  font-size: 18px;
  margin-bottom: 5px;
  font-weight: bold;
}

.board-content {
  margin-bottom: 10px;
}

.detail-link {
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
  text-decoration: none;

}

.detail-link:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
}

.detail-link:active {
  box-shadow: inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
}

</style>
