import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const userInfo = ref([]) // Store user information
  const boards = ref([])
  const isLogin = computed(() => {
    return token.value !== null && token.value !== undefined
  })
  const state_s = {
    savingsData: null // 받은 데이터를 저장할 상태
  }

  const state_d = {
    DepositData: null // 받은 데이터를 저장할 상태
  }

  const exchangeRateData = ref({
    amount: ref(0),
    selectedCurrency: ref(''),
    convertedAmount: ref(0),
    currencies: ref([])
  })
  
  const exchangeRateDataKor = ref({
    amount: ref(0),
    selectedCurrency: ref(''),
    convertedAmount: ref(0),
    currencies: ref([])
  })

  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('token') || null);

  const getBoards = function () {
    axios({
      method: 'get',
      url: `${API_URL}/boards/`,
      headers: {
        Authorization:`Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        boards.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  

  const signUp = function(payload) {
    const { username, email, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        email,
        password1,
        password2
      }
    })
      .then((res)=>{
        console.log(res.data)
        const password = password1
        logIn({username, password})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function(payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((res)=>{
        token.value = res.data.key
        localStorage.setItem('token', res.data.key); // 토큰을 로컬 스토리지에 저장
        getUserInfo(username);
        router.push({ name: 'MainPageView' });
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  const logOut = function() {
    localStorage.removeItem('token');
    token.value = null;
    router.push({ name: 'LogInView' });
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`, // 로그아웃 엔드포인트 URL
      data : { 
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        token.value = null; // 토큰 삭제 또는 초기화
        router.push({ name: 'LogInView' }); // 로그인 화면으로 리다이렉트
      })
      .catch((err) => {
        console.error(err);
      });
  };



  const getUserInfo = () => {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/profile/`, // Endpoint to get user info by username
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userInfo.value = res.data // Save user info in store
        // console.log(res.data)

      })
      .catch((err) => {
        console.error(err)
      })
  }

  const loading = ref(false)
  const userProduct = ref({
    saving_rates : ref([]),
    max_rates : ref([]),
    average_saving_rate : ref(0),
    average_max_rate: ref(0),
    fin_prdt_nms: ref([])
  })


  const getUserChart = async () => {
    if (!loading.value) {
      loading.value = true;
  
      try {
        const response = await axios.get(`${API_URL}/accounts/user/chart/`, {
          headers: {
            Authorization: `Token ${token.value}`,
          },
        });
  
        userProduct.value.saving_rates = response.data.saving_rates;
        userProduct.value.max_rates = response.data.max_rates;
        userProduct.value.average_saving_rate = response.data.average_saving_rate;
        userProduct.value.average_max_rate = response.data.average_max_rate;
        userProduct.value.fin_prdt_nms = response.data.fin_prdt_nms;
  
        // console.log(response.data);
        // drawChart();
      } catch (error) {
        console.error(error);
      } finally {
        loading.value = false;
      }
    }
  };


  const updateUserInfo = async (field, value) => {
    try {
      const response = await axios.patch(
        `${API_URL}/accounts/user/update/`,
        { [field]: value },
        { headers: { Authorization: `Token ${token.value}` } }
      );
      await getUserInfo();
    } catch (error) {
      console.error(error);
    }
  };


  const actions_s = {
    async getSavings() {
      try {
        const response = await axios.get(`${API_URL}/finlife/s/`)
        state_s.savingsData = response.data // 받은 데이터를 상태에 저장
        return response.data // 받은 데이터 반환
      } catch (error) {
        console.error(error)
        throw error
      }
    },
  }

  const actions_d = {
    async getDeposit() {
      try {
        const response = await axios.get(`${API_URL}/finlife/d/`)
        state_d.DepositData = response.data // 받은 데이터를 상태에 저장
        return response.data // 받은 데이터 반환
      } catch (error) {
        console.error(error)
        throw error
      }
    },
  }
  
  const actions_exchange = {
    async setCurrencies() {
      try {
        const response = await axios.get(`${API_URL}/currency/exchange/`)
  
        const currencies = response.data.map(currency => ({
          cur_unit: currency.cur_unit,
          cur_nm: currency.cur_nm,
        }))
  
        exchangeRateData.value.currencies = currencies
      } catch (error){
        console.error(error)
      }
    }
  }


  const convertToKOR = function(payload) {
    const { amount, selectedCurrency } = payload
    console.log("counter",payload)
    axios({
      method: 'post',
      url: `${API_URL}/currency/to_kor/`,
      data: {
        amount,
        selectedCurrency
      }
    })
      .then((response)=>{
        exchangeRateData.value.convertedAmount = response.data.converted_amount
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const convertToCurrency = function(payload) {
    const { korAmount, selectedCurrencyKor } = payload
    console.log("counter",payload)
    axios({
      method: 'post',
      url: `${API_URL}/currency/kor_to/`,
      data: {
        korAmount,
        selectedCurrencyKor
      }
    })
      .then((response)=>{
        exchangeRateDataKor.value.convertedAmount = response.data.converted_amount
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { 
    boards,
    API_URL,
    signUp, 
    logIn, 
    token, 
    isLogin, 
    logOut, 
    getUserInfo, 
    userInfo, 
    getBoards,
    ...state_s,
    ...actions_s,
    ...state_d,
    ...actions_d,
    exchangeRateData,
    exchangeRateDataKor,
    ...actions_exchange,
    convertToCurrency,
    convertToKOR,
    getUserChart,
    userProduct,
    updateUserInfo
  }
}, {persist: true})
