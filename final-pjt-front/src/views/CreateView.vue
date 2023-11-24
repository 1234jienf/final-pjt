<template>
  <div class="article-form">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" class="form">
      <div class="form-group">
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title" class="form-control">
      </div>
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn-submit">작성하기</button>
      <button @click="goBack" class="btn-back">게시물 목록 보기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref('')
const content = ref('')
const store = useCounterStore()
const router = useRouter()

const createArticle = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/boards/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(() => {
    router.push({ name: 'BoardView' })
  })
  .catch((err) => {
    console.log(err)
  })
}

const goBack = () => {
  router.go(-1); // 이전 페이지로 이동
}
</script>

<style scoped>
.article-form {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
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

*{
  font-family:'SpoqaHanSansNeo-Medium',sans-serif;
}
.btn-submit {
  padding: 8px 15px;
  background-color: #5a95d4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: large;
  font-family:'SpoqaHanSansNeo-Thin',sans-serif;

}

.btn-submit:hover {
  background-color: #0056b3;
}

.btn-back{
  background: none;
  border: none;
  text-align: center;
  color: whitesmoke;
  background-color: #1f1f47;
  padding: 0.1rem 0.5rem;
  border-radius: 0.2rem;
  cursor: pointer;
  font-family: 'SpoqaHanSansNeo-Thin', sans-serif;
  font-size: large;
  border-radius: 0.1rem;
}

.btn2 {
  background: none;
  border: none;
  text-align: center;
  font-size: 1rem;
  color: whitesmoke;
  background-color: #fa709a;
  padding: 0.8rem 1.8rem;
  border-radius: 2rem;
  text-decoration: none;
  cursor: pointer;
  
}
</style>
