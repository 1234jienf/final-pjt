<template>
  <div class="board-list">
    <h3>게시물 목록 보기</h3>
    <div class="board-items">
      <BoardListItem 
        v-for="board in store.boards"
        :key="board.id"
        :board="board"
      />
    </div>
  </div>
</template>
  
<script setup>
import { useCounterStore } from '@/stores/counter'
import BoardListItem from '@/components/BoardListItem.vue'
  
const store = useCounterStore()
console.log(store.boards)
</script>

<style scoped>
/* Board List 스타일 */
.board-list {
  margin-top: 20px;
}

.board-items {
  display: grid;
  border-radius: 20px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  padding: 3px 3px 3px 3px;
  overflow: hidden;
}

</style>
