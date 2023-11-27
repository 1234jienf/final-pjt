<template>

  <div class="login-container">
    
    <h1>로그인</h1>
    <div class="blob"></div>
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
  color: black;
  text-shadow: 1px 1px 1px #FFF;
}

.login-container {
  width: 350px;
  padding: 16px;
  margin: 0 auto;
  text-align: center;
  background: #BABECC;
  padding: 3em;
  height: 320px;
  border-radius: 20px;
  border-left: 1px solid white;
  border-top: 1px solid white;
  backdrop-filter: blur(10px);
  box-shadow: 20px 20px 40px -6px rgba(0,0,0,0.2);
  text-align: center;
  position: relative;
  transition: all 0.2s ease-in-out;
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

.blob {
  position: absolute;
  width: 500px;
  height: 500px;
  background: linear-gradient(
    180deg,
    rgba(47, 184, 255,0.42) 31.77%,
    #5c9df1 100%
  );
  mix-blend-mode: color-dodge;
  -webkit-animation: move 25s infinite alternate;
          animation: move 25s infinite alternate;
  transition: 1s cubic-bezier(0.07, 0.8, 0.16, 1);
}

.blob:hover {
  width: 520px;
  height: 520px;
  -webkit-filter: blur(30px);
          filter: blur(30px);
  box-shadow:
    inset 0 0 0 5px rgba(255,255,255, 0.6),
    inset 100px 100px 0 0px #fa709a,
    inset 200px 200px 0 0px #784ba8,
    inset 300px 300px 0 0px #2b86c5;
}

@-webkit-keyframes move {
  from {
    transform: translate(-100px, -50px) rotate(-90deg);
    border-radius: 24% 76% 35% 65% / 27% 36% 64% 73%;
  }

  to {
    transform: translate(500px, 100px) rotate(-10deg);
    border-radius: 76% 24% 33% 67% / 68% 55% 45% 32%;
  }
}

@keyframes move {
  from {
    transform: translate(-100px, -50px) rotate(-90deg);
    border-radius: 24% 76% 35% 65% / 27% 36% 64% 73%;
  }

  to {
    transform: translate(500px, 100px) rotate(-10deg);
    border-radius: 76% 24% 33% 67% / 68% 55% 45% 32%;
  }
}
</style>
