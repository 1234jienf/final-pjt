import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import BoardView from '@/views/BoardView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import UpdateView from '@/views/UpdateView.vue'
import LogInView from '@/views/LogInView.vue'
import CulculatorView from '@/views/CalculatorView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SavingView from '@/views/SavingView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'
import KakaomapView from '@/views/KakaomapView.vue'
import RecommendedProductsView from '@/views/RecommendedProductsView.vue';
import { useCounterStore } from '../stores/counter'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/boards',
      name: 'BoardView',
      component: BoardView
    },
    {
      path: '/boards/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/boards/:id/update',
      name: 'UpdateView',
      component: UpdateView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/',
      name: 'MainPageView',
      component: MainPageView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/calculator',
      name: 'CalculatorView',
      component: CulculatorView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/savingdeposit',
      name: 'SavingView',
      component: SavingView,
    },
    {
      path: '/deposit',
      name: 'DepositView',
      component: DepositView,
    },
    {
      path: '/deposit-detail/:fin_prdt_cd',
      name: 'DepositDetailView',
      component: DepositDetailView
    },
    {
      path: '/saving-detail/:fin_prdt_cd',
      name: 'SavingDetailView',
      component: SavingDetailView
    },
    {
      path: '/kakaomapview',
      name: 'KakaomapView',
      component: KakaomapView
    },
    {
      path: '/recommended-products',
      name: 'RecommendedProductsView',
      component: RecommendedProductsView,
    },
  ],

})

router.beforeEach((to,from) => {
  const store = useCounterStore() 
  if (to.name === 'BoardView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return {name: 'LoginView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'MainPageView'}
  }
})


export default router


