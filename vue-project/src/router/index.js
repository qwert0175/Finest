import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignupView from '@/views/SignupView.vue'
import MapView from '@/views/MapView.vue'
import ProductView from '@/views/ProductView.vue'
import RecommendView from '@/views/RecommendView.vue'
import CommunityView from '@/views/CommunityView.vue'
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
      path: '/productview',
      name: 'productview',
      component: ProductView
    },
    {
      path: '/recommendview',
      name: 'recommendview',
      component: RecommendView
    },
    {
      path: '/communityview',
      name: 'communityview',
      component: CommunityView
    },
    {
      path: '/finestsignupview',
      name: 'finestsignupview',
      component: FinestSignupView
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

export default router
