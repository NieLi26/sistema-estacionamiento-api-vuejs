import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CheckIn from '../views/CheckIn.vue'
import CheckOut from '../views/CheckOut.vue'
import SignIn from '../views/SignIn.vue'
import SignUp from '../views/SignUp.vue'
import Reserves from '../views/Reserves.vue'
import Tarif from '../views/Tarif.vue'
import TarifPeriod from '../views/TarifPeriod.vue'
import Client from '../views/Client.vue'
import Payments from '../views/Payments.vue'
import ReservePeriod from '../views/ReservePeriod.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/checkin',
      name: 'checkin',
      component: CheckIn
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: CheckOut
    },
    {
      path: '/reserve-period',
      name: 'reserve-period',
      component: ReservePeriod
    },
    {
      path: '/signin',
      name: 'signin',
      component: SignIn
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/reserves',
      name: 'reserves',
      component: Reserves
    },
    {
      path: '/tarif',
      name: 'tarif',
      component: Tarif
    },
    {
      path: '/tarif-period',
      name: 'tarif-period',
      component: TarifPeriod
    },
    {
      path: '/client',
      name: 'client',
      component: Client
    },
    {
      path: '/payments',
      name: 'payments',
      component: Payments
    },
  ],
  linkActiveClass: 'bg-gray-100 text-gray-900'
})

export default router
