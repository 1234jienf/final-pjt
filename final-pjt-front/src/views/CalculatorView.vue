<template>
  <div class="calculator-container">
    <div class="calculator">
    <h1>환율 계산기 (타국 통화 변환)</h1>
    <div>
      <label for="amount">금액:</label>
      <input v-model="amount" type="number" id="amount">
    </div>
    <label for="currency">통화</label>
    <select v-model="selectedCurrency" id="currency" @change="selectCurrency">
      <option v-for="currency in exchangeRateData.currencies" :key="currency.cur_unit" :value="currency.cur_unit">
        {{ currency.cur_nm }}
      </option>
    </select>
    <button @click="handleConversion">환전</button>
    <p>{{ exchangeRateData.convertedAmount }} 원</p>
  </div>
  <div class="calculator">
    <h1>환율 계산기 (원화 변환)</h1>
    <div>
      <label for="korAmount">금액:</label>
      <input v-model="korAmount" type="number" id="korAmount">
    </div>
    <label for="currencyKor">통화</label>
    <select v-model="selectedCurrencyKor" id="currencyKor" @change="selectCurrencyKor">
      <option v-for="currency in exchangeRateData.currencies" :key="currency.cur_unit" :value="currency.cur_unit">
        {{ currency.cur_nm }}
      </option>
    </select>

    <button @click="handleConversionKor">환전</button>

    <p>{{ exchangeRateDataKor.convertedAmount }} {{ selectedCurrencyKor }}</p>
  </div>
</div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

const amount = ref(null)
const korAmount = ref(null)
const selectedCurrency = ref(null)
const selectedCurrencyKor = ref(null)
const exchangeRateData = ref(null)
const exchangeRateDataKor = ref(null)

exchangeRateData.value =  store.exchangeRateData
exchangeRateDataKor.value =  store.exchangeRateDataKor


const handleConversion = async () => {
  const payload = {
    amount: amount.value,
    selectedCurrency: selectedCurrency.value
  }

  try {
      await store.convertToKOR(payload)
  } catch(error) {
    console.error(error)
  }
}

const handleConversionKor = async () => {
  const payload = {
    korAmount: korAmount.value,
    selectedCurrencyKor: selectedCurrencyKor.value
  }

  try {
      await store.convertToCurrency(payload)
  } catch(error) {
    console.error(error)
  }
}

const selectCurrency = (currency) => {
  const selectedValue = currency.target.value
  exchangeRateData.selectedCurrency = selectedValue
  console.log("selectedCurreny:", exchangeRateData.selectedCurrency)
}

const selectCurrencyKor = (currencyKor) => {
  const selectedValueKor = currencyKor.target.value
  exchangeRateDataKor.selectedCurrency = selectedValueKor
  console.log("selectedCurreny:", exchangeRateDataKor.selectedCurrency)
};

onMounted(async () => {
  // setCurrencies 함수의 실행을 기다린 후에 로그를 출력
  await store.setCurrencies();
  console.log("exchangeRateData:", exchangeRateData);
});


</script>

<style scoped>
  .calculator-container {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #EAEFFE;
    height: 100vh;
  }

  .calculator {
    border: 1px solid #526ADF;
    border-radius: 8px;
    padding: 16px;
    margin: 0 50px 20px 50px;
    background-color: white;
    width: 400px;
    transition: transform 0.3s, box-shadow 0.3s;
    transform-style: preserve-3d; 
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  }

  .calculator:hover {
    transform: translateY(-10px);
    box-shadow: 0px 12px 20px rgba(0, 0, 0, 0.2);
  }

  h1 {
    font-size: 1.5em;
    margin-bottom: 10px;
  }

  label {
    display: block;
    margin-bottom: 6px;
  }

  input,
  select {
    width: 100%;
    padding: 8px;
    margin-bottom: 12px;
    box-sizing: border-box;
  }

  button {
    background-color: #526ADF;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }

  button:hover {
    background-color: #526ADF;
  }

  p {
    margin-top: 10px;
    font-size: 1.2em;
  }
</style>