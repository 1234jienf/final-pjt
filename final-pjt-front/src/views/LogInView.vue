<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="form">
      <label>
        <input type="text" v-model.trim="username" placeholder="UserName" class="input-field">
      </label>
      <label>
        <input type="password" v-model.trim="password" placeholder="Password" class="input-field">
      </label>
      <button type="submit" class="red">LOGIN</button>
    </form>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>
/* 공통 스타일 */
h1 {
  color: #BABECC;
  text-shadow: 1px 1px 1px #FFF;
}

.login-container {
  width: 350px;
  padding: 16px;
  margin: 0 auto;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 24px;
  width: 100%;
}

.input-field {
  margin-right: 8px;
  padding: 16px;
  border: none;
  border-radius: 20px;
  box-shadow: inset 2px 2px 5px #BABECC, inset -5px -5px 10px #FFF;
  width: 100%;
  box-sizing: border-box;
  transition: all 0.2s ease-in-out;
}

input[type="password"] {
  margin-bottom: 24px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px;
}

button {
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

button.red {
  display: block;
  width: 100%;
  color: #AE1100;
}

button:hover {
  box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
}

button:active {
  box-shadow: inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
}
</style>
