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
  border: none;
  outline: none;
  font-size: 10px;
  border-radius: 20px;
  background-color: #EBECF0;
  text-shadow: 1px 1px 0 #FFF;
  cursor: pointer;
  box-shadow: -5px -5px 20px #FFF, 5px 5px 20px #BABECC;
  transition: all 0.2s ease-in-out;
  position: relative;

}

.detail-link:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
}

.detail-link:active {
  box-shadow: inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
}

</style>
