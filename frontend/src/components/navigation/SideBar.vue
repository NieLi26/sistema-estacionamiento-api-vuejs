<template>
    <!--
      This example requires updating your template:
  
      ```
      <html class="h-full bg-gray-100">
      <body class="h-full">
      ```
    -->
    <div>
      <TransitionRoot as="template" :show="sidebarOpen">
        <Dialog as="div" class="fixed inset-0 flex z-40 md:hidden" @close="sidebarOpen = false">
          <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100" leave-to="opacity-0">
            <DialogOverlay class="fixed inset-0 bg-gray-600 bg-opacity-75" />
          </TransitionChild>
          <TransitionChild as="template" enter="transition ease-in-out duration-300 transform" enter-from="-translate-x-full" enter-to="translate-x-0" leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0" leave-to="-translate-x-full">
            <div class="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-white">
              <TransitionChild as="template" enter="ease-in-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-300" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 right-0 -mr-12 pt-2">
                  <button type="button" class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" @click="sidebarOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x h-6 w-6 text-white" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                  </button>
                </div>
              </TransitionChild>
              <div class="flex-shrink-0 flex items-center px-4">
                <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/workflow-logo-indigo-600-mark-gray-800-text.svg" alt="Workflow" />
              </div>
              <div class="mt-5 flex-1 h-0 overflow-y-auto">
                <nav class="px-2 space-y-1">
                    <template  v-for="item in navigation" >
                        <template v-if="item.subMenu !== undefined">
                            <details class="group">
                                <summary
                                class="cursor-pointer text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                                >
                                <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />

                                {{ item.name }}

                                <span
                                    class="ml-auto shrink-0 transition duration-300 group-open:-rotate-180"
                                >
                                    <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-5 w-5"
                                    viewBox="0 0 20 20"
                                    fill="currentColor"
                                    >
                                    <path
                                        fill-rule="evenodd"
                                        d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                        clip-rule="evenodd"
                                    />
                                    </svg>
                                </span>
                                </summary>

                                <nav class="mt-1.5 ml-8 flex flex-col">
                                <RouterLink
                                    v-for="sub in item.subMenu"
                                    :to="{path: sub.to}"
                                    class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                                >
                                <component :is="sub.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />

                                    <span class="ml-3 text-sm font-medium"> {{ sub.name }}</span>
                                </RouterLink>
                                </nav>
                            </details>
                        </template>
                        <template v-else>
                            <RouterLink :key="item.name" :to="{path: item.to}" class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md">
                                <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />
                                {{ item.name }}
                            </RouterLink>
                        </template>
                    </template>
                </nav>
              </div>
            </div>
          </TransitionChild>
          <div class="flex-shrink-0 w-14" aria-hidden="true">
            <!-- Dummy element to force sidebar to shrink to fit close icon -->
          </div>
        </Dialog>
      </TransitionRoot>
  
      <!-- Static sidebar for desktop -->
      <div class="hidden md:flex md:w-64 md:flex-col md:fixed md:inset-y-0">
        <!-- Sidebar component, swap this element with another sidebar if you like -->
        <div class="flex flex-col flex-grow border-r border-gray-200 pt-5 bg-white overflow-y-auto">
          <div class="flex items-center flex-shrink-0 px-4">
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/workflow-logo-indigo-600-mark-gray-800-text.svg" alt="Workflow" />
          </div>
          <div class="mt-5 flex-grow flex flex-col">
            <nav class="flex-1 px-2 pb-4 space-y-1">
                <template  v-for="item in navigation" >
                    <template v-if="item.subMenu !== undefined">
                        <details class="group">
                            <summary
                            class="cursor-pointer text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                            >
                            <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />

                            {{ item.name }}

                            <span
                                class="ml-auto shrink-0 transition duration-300 group-open:-rotate-180"
                            >
                                <svg
                                xmlns="http://www.w3.org/2000/svg"
                                class="h-5 w-5"
                                viewBox="0 0 20 20"
                                fill="currentColor"
                                >
                                <path
                                    fill-rule="evenodd"
                                    d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                    clip-rule="evenodd"
                                />
                                </svg>
                            </span>
                            </summary>

                            <nav class="mt-1.5 ml-8 flex flex-col">
                            <RouterLink
                                v-for="sub in item.subMenu"
                                :to="{path: sub.to}"
                                class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                            >
                                <component :is="sub.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />

                                <span class="ml-3 text-sm font-medium"> {{ sub.name }}</span>
                            </RouterLink>
                            </nav>
                        </details>
                    </template>
                    <template v-else>
                        <RouterLink :key="item.name" :to="{path: item.to}" class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md">
                            <component :is="item.icon" class="mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />
                            {{ item.name }}
                        </RouterLink>
                    </template>
                </template>
            </nav>
            
          </div>
        </div>
      </div>
      
      <div class="md:pl-64 flex flex-col flex-1">
        <!-- Navbar -->
        <div class="sticky top-0 z-10 flex-shrink-0 flex h-16 bg-white shadow">
            <!-- Open sidebar mobile -->
          <button type="button" class="px-4 border-r border-gray-200 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500 md:hidden" @click="sidebarOpen = true">
            <span class="sr-only">Open sidebar</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5" />
            </svg>

          </button>
          <!-- Navbar menu -->
          <div class="flex-1 px-4 flex justify-between">
            <!-- Search -->
            <div class="flex-1 flex items-center">
                <RouterLink class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 group flex items-center px-2 py-2 text-sm font-medium rounded-md" to="/">Home</RouterLink>
            </div>
            <div class="mr-4 flex items-center md:mr-6">
                <button
              @click="toggleDark()" 
                class="relative inline-flex h-6 w-11 items-center rounded-full dark:bg-gray-600 bg-gray-300"
   
              >
                <span class="sr-only">Enable notifications</span>

                <span
       
                  class="transform rounded-full transition p-1 bg-white  text-gray-800  dark:bg-gray-800  dark:text-white dark:translate-x-6 translate-x--1"
                >
                <svg  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                    <path v-if="isDark" stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
                    <path v-else stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
                </svg>
                </span>
                </button>
            </div>
            <!-- dropdown -->
            <div class="ml-4 flex items-center md:ml-6">
              <button type="button" class="bg-white p-1 rounded-full text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                <span class="sr-only">View notifications</span>
                <BellIcon class="h-6 w-6" aria-hidden="true" />
              </button>
  
              <!-- Profile dropdown -->
              <Menu as="div" class="ml-3 relative">
                <div>
                  <MenuButton class="max-w-xs bg-white flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    <span class="sr-only">Open user menu</span>
                    <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                  </MenuButton>
                </div>
                <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                  <MenuItems class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <!-- <MenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
                      <a :href="item.href" :class="[active ? 'bg-gray-50' : '', 'block px-4 py-2 text-sm text-gray-600']">{{ item.name }}</a>
                    </MenuItem> -->
                    <MenuItem v-if="useAuthStore().user.isAuthenticated" v-slot="{ active }">
                      <a href="#" @click="logout" :class="[active ? 'bg-gray-50' : '', 'block px-4 py-2 text-sm text-gray-600']">Sign out</a>
                    </MenuItem>
                    <template v-if="!useAuthStore().user.isAuthenticated">
                      <RouterLink class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 block px-4 py-2 text-sm" to="/signup">Sign up</RouterLink>
                      <RouterLink class="text-gray-600 hover:bg-gray-50 hover:text-gray-900 block px-4 py-2 text-sm" to="/signin">Sign in</RouterLink>
                    </template>     
                  </MenuItems>
                </transition>
              </Menu>
            </div>
          </div>
        </div>
  
        <main class="flex-1">
          <div class="py-6">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
              <h1 class="text-2xl font-semibold text-gray-900">Dashboard</h1>
            </div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
              <!-- Replace with your content -->
              <div class="py-4">
                <!-- <div class="border-4 border-dashed border-gray-200 rounded-lg h-96" /> -->
                <RouterView />
              </div>
              <!-- /End replace -->
            </div>
          </div>
        </main>
      </div>
    </div>
</template>


<script setup>
import { ref } from 'vue'
import { RouterView } from 'vue-router'
import {
  Dialog,
  DialogOverlay,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'

import { RouterLink } from 'vue-router'
import router from '../../router';
import { useAuthStore } from '../../stores/auth';
import axios from "axios";
import AuthAPI from '../../services/AuthAPI';
import { useDark, useToggle } from '@vueuse/core'

import {
  BellIcon,
  CalendarDaysIcon,
  ChartBarIcon,
  FolderIcon,
  HomeIcon,
  InboxIcon,
  UserIcon,
  MagnifyingGlassIcon,
  WrenchScrewdriverIcon,
  ArrowRightOnRectangleIcon,
  ArrowLeftOnRectangleIcon
  
} from '@heroicons/vue/24/outline'


import { ParkingIcon, BookIcon, ClockHour3Icon, BrandCashappIcon, CalendarPlusIcon } from 'vue-tabler-icons';


const navigation = [
  { name: 'Estacionamiento', to: '#', icon: ParkingIcon, subMenu: [{name: 'Entrada', to:'/checkin', icon: ArrowRightOnRectangleIcon}, {name: 'Salida', to:'/checkout', icon: ArrowLeftOnRectangleIcon},   { name: 'Agendar', to: '/reserve-period', icon: CalendarPlusIcon},]},
  { name: 'Registro', to: '#', icon: BookIcon, subMenu: [{name: 'Por Hora', to:'/reserves', icon: ClockHour3Icon}]},
  { name: 'Mantenimiento', to: '#', icon: WrenchScrewdriverIcon, subMenu: [{name: 'Tarifa', to:'/tarif'}, {name: 'Tarifa plan', to:'/tarif-period'}, {name: 'Cliente', to:'/client'}]},
  { name: 'Pagos', to: '/payments', icon: BrandCashappIcon},
]

const userNavigation = [
  { name: 'Your Profile', href: '#' },
  { name: 'Settings', href: '#' },
//   { name: 'Sign out', href: '#' },
]

const sidebarOpen = ref(false)


const logout = async () => {

// para borrar el token de la BBDD  
AuthAPI.logoutUser()
.then(res => console.log('logout'))
// restablecemos la informacion del usuario cada ves que se loge 
axios.defaults.headers.common['Authorization'] = ""
// removemos el token del localstorage, en caso de que tenga un token de una sesion antetioro
localStorage.removeItem('token')
// remover todo del store
useAuthStore().removeToken()

router.push("/signin")
}

// dark mode toggle
// base css
const isDark = useDark() 
const toggleDark = useToggle(isDark)



</script>