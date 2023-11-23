<template>
  <div>
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
    </div>
    <div>
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
.calculator {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 20px;
  background-color: #f9f9f9;
}
</style>
