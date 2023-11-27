<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <label>
        <input type="text" v-model.trim="username" placeholder="UserName" class="input-field">
      </label>
      <label>
        <input type="password" v-model.trim="password1" placeholder="Password" class="input-field">
      </label>
      <label>
        <input type="password" v-model.trim="password2" placeholder="Password Confirm" class="input-field" @input="checkPasswordMatch">
        <span v-if="passwordMismatch" style="color: red;">비밀번호가 일치하지 않습니다.</span>
      </label>
      <label>
        <input type="text" v-model.trim="email" placeholder="Email Address" class="input-field">
      </label>
      <label>
        <input type="nickname" v-model.trim="nickname" placeholder="nickname" class="input-field">
      </label>
      <label>
        <input type="age" v-model.trim="age" placeholder="age" class="input-field">
      </label>
      <label>
        <input type="money" v-model.trim="money" placeholder="money" class="input-field">
      </label>
      <label>
        <input type="salary" v-model.trim="salary" placeholder="salary" class="input-field">
      </label>
      <label>
        <input type="financial_products" v-model.trim="financial_products" placeholder="financial_products" class="input-field">
      </label>
      <button class="red" type="submit">SIGN IN</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const financial_products = ref(null)


const passwordMismatch = ref(false);

const checkPasswordMatch = function() {
  if (password1.value !== password2.value) {
    passwordMismatch.value = true;
  } else {
    passwordMismatch.value = false;
  }
}

const signUp = function() {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: parseInt(age.value),
    money: parseInt(money.value),
    salary: parseInt(salary.value),
    financial_products:financial_products.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
.signup-container {
  width: 350px;
  padding: 16px;
  margin: 0 auto;
  text-align: center;
}

h1 {
  color: #BABECC;
  text-shadow: 1px 1px 1px #FFF;
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

.unit {
  border-radius: 8px;
  line-height: 0;
  width: 48px;
  height: 48px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 4px;
  font-size: 19.2px;
}

</style>
