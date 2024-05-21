import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import UpdateInfoView from '@/views/UpdateInfoView.vue'
import SignupView from '@/views/SignupView.vue'
import MapView from '@/views/MapView.vue'
import ProductView from '@/views/ProductView.vue'
import DepositDetail from '@/views/DepositDetail.vue'
import SavingDetail from '@/views/SavingDetail.vue'
import RecommendView from '@/views/RecommendView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CreateView from '@/views/CreateView.vue'
import DetailView from '@/views/DetailView.vue'
import UpdateView from '@/views/UpdateView.vue'
import FinestSignupView from '@/views/FinestSignupView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homeview',
      component: HomeView
    },
    {
      path: '/loginview',
      name: 'loginview',
      component: LoginView
    },
    {
      path: '/updateinfo',
      name: 'updateinfo',
      component: UpdateInfoView
    },
    {
      path: '/signupview',
      name: 'signupview',
      component: SignupView
    },
    {
      path: '/mapview',
      name: 'mapview',
      component: MapView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/depositdetail/:id',
      name: 'depositdetail',
      component: DepositDetail
    },
    {
      path: '/savingdetail/:id',
      name: 'savingdetail',
      component: SavingDetail
    },
    {
      path: '/recommendview',
      name: 'recommendview',
      component: RecommendView
    },
    {
      path: '/finestsignupview',
      name: 'finestsignupview',
      component: FinestSignupView
    },
    {
      path: '/communityview',
      name: 'communityview',
      component: CommunityView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/detailview/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/detailview/:id/update',
      name: 'UpdateView',
      component: UpdateView
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

import { useUserInfoStore } from '@/stores/userinfo'


router.beforeEach((to, from) => {
  const store = useUserInfoStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  // if (to.name === 'ArticleView' && store.isLogin === false) {
  //   window.alert('로그인이 필요해요!!')
  //   return { name: 'LogInView' }
  // }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'communityview' }
  }
})

export default router
