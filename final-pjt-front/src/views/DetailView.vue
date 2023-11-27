<template>
  <div class="detail">
    <h1>Detail</h1>
    <div v-if="board" class="board-details">
      <p>제목 : {{ board.title }}</p>
      <p>내용 : {{ board.content }}</p>
      <p>작성일 : {{ board.created_at }}</p>
      <p>수정일 : {{ board.updated_at }}</p>
      <div v-if="CurrentUser" class="buttons">
        <button @click="deleteBoard" class="delete-btn">삭제</button>
        <button @click="updateBoard" class="update-btn">수정</button>
          </div>
        </div>
        <form @submit.prevent="addComment">
          <div class="">
          <label for="comment"></label>
          <textarea v-model="commentText" id="comment" rows="4" cols="50"></textarea>
          <button type="submit" class="btn-submit">댓글쓰기</button>
        </div>
        </form>
        <!-- Display Comments -->
        <div v-if="comments && comments.length">
          <h3>Comments:</h3>
          <div v-for="comment in comments" :key="comment.id" class="comment">
            <div class="comment-header">
              <span class="comment-author">{{ comment.username }}</span>
              <span class="comment-date">{{ comment.created_at }}</span>
            </div>
            <p class="comment-content">{{ comment.content }}</p>
            <button v-if="comment.username === store.userInfo.username" @click="deleteComment(comment.id)" class="delete-btn">삭제</button>
          </div>
        </div>
        <button @click="goBack" class="btn-back">게시물 목록 보기</button>
      </div>
</template>
  
<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const board = ref(null)
const commentText = ref('')
const comments = ref([])


const fetchComments = () => {
axios({
  method: 'get',
  url: `${store.API_URL}/boards/${route.params.id}/comment/`
})
  .then((res) => {
    comments.value = res.data
  })
  .catch((err) => {
    console.log(err)
    console.log(comments.value)
  })
}

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/boards/${route.params.id}/`
  })
    .then((res) => {
      board.value = res.data
      comments.value = board.value.comments
      console.log(comments.value)
      console.log(board.value.author)
    })
    .catch((err) => {
      console.log(err)
    })
    store.getUserInfo()

})

// onMounted(fetchComments)



const addComment = () => {
axios({
  method: 'post',
  url: `${store.API_URL}/boards/${route.params.id}/comment/`,
  data: { content: commentText.value },
  headers: {
    Authorization: `Token ${store.token}`
  }
})
  .then(() => {
    fetchComments() // 새로운 댓글 추가 후 댓글 목록 새로고침
    commentText.value = '' // 제출 후 댓글 필드 비우기
  })
  .catch((err) => {
    console.log(err)
  })
}

// Function to delete a comment
const deleteComment = (commentId) => {
axios({
  method: 'delete',
  url: `${store.API_URL}/boards/${route.params.id}/comment/${commentId}/`,
  headers: {
    Authorization: `Token ${store.token}`
  }
})
  .then(() => {
    fetchComments() // Refresh comments after deleting one
    console.log()
  })
  .catch((err) => {
    console.log(err)
  })
}

const CurrentUser = computed(() => {
  return store.userInfo.id === board.value.author

})

const deleteBoard = () => {
  if (board.value && confirm('정말로 이 게시글을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/boards/${route.params.id}/delete/`,
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
}

const updateBoard = () => {
  router.push({
    name: 'UpdateView',
    query: {
      id: board.value.id,
      title: board.value.title,
      content: board.value.content
    }
  })
}


const goBack = () => {
  router.go(-1)
}
</script>
  
<style scoped>
.detail {
padding: 20px;
}

.board-details {
border: 1px solid #ccc;
padding: 20px;
margin-bottom: 20px;
}

.buttons {
margin-top: 10px;
}

.delete-btn,
.update-btn,
.back-btn {
padding: 8px 16px;
border: none;
border-radius: 5px;
color: white;
cursor: pointer;
}

.delete-btn {
background-color: #dc3545; /* 빨간색 */
}

.update-btn {
background-color: #007bff; /* 파란색 */
}
.back-btn{
  background-color: #00ffb3; /* 파란색 */
}

.delete-btn:hover,
.update-btn:hover {
filter: brightness(1.2); /* 호버 시 밝기 조정 */
}

.back-btn:hover{
  filter: brightness(1.2);
}

.comment {
border: 1px solid #eee;
padding: 10px;
margin-bottom: 10px;
}

*{
  font-family: 'SpoqaHanSansNeo-Medium',sans-serif ;
}
.comment-header {
display: flex;
justify-content: space-between;
margin-bottom: 5px;
}

.comment-author {
font-weight: bold;
}

.comment-date {
color: #888;
}

.comment-content {
margin-top: 5px;
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

</style>