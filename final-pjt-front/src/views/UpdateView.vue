<template>
  <div class="update-article">
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle" class="form">
      <div class="form-group">
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title" class="form-control">
      </div>
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn-update">게시글 수정</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const route = useRoute()
const router = useRouter()
const title = ref('')
const content = ref('')
const store = useCounterStore()

onMounted(() => {
  axios.get(`${store.API_URL}/boards/${route.params.id}/`)
    .then(response => {
      title.value = response.data.title
      content.value = response.data.content
    })
    .catch(error => {
      console.error(error)
    })
})

const updateArticle = () => {
  axios.put(`${store.API_URL}/boards/${route.params.id}/update/`, {
      title: title.value,
      content: content.value
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then(() => {
      router.push({ name: 'BoardView'})
    })
    .catch(error => {
      console.error(error)
    })
}
</script>

<style scoped>
.update-article {
  padding: 20px;
}

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
  font-size: 16px;
}

.btn-update {
  padding: 8px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-update:hover {
  background-color: #0056b3;
}
</style>
