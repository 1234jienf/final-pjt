<!-- components/RecommendedProducts.vue -->

<template>
  <div class="recommended-products">
    <h1>추천 상품</h1>
    <ul>
      <li v-for="product in recommendedProducts" :key="product.id">{{ product.name }} - {{ product.rate }}</li>
    </ul>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted, ref } from 'vue';

const store = useCounterStore()
const recommendedProducts = ref([])

onMounted(async () => {
  await store.getRecommendedProducts();
  recommendedProducts.value = store.recommendedProducts.value
});

// async function store.getRecommendedProducts() {
//   await store.getRecommendedProducts();
// }
</script>

<style scoped>
/* 필요한 스타일링을 추가하거나 수정 */
</style>
