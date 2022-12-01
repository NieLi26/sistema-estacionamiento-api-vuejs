<script setup>
// import axios from 'axios'
import { ref } from 'vue';
import CheckOutAPI from '@/services/checkout/CheckOutAPI';
import Modal from "@/components/checkout/Modal.vue";

const lots = ref('')

const loadLots = async () => {
  try {
    // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
    const response = await CheckOutAPI.getCheckOut();
    // setTimeout(() => {
    lots.value = response.data
    // }, 3000)
  } catch (error) {
    console.log(error);
  }

}

loadLots()


const colorLot = (status) => {

  if (status === 'av') {
    return 'bg-green-300 hover:bg-green-200'
  } else if (status === 're') {
    return 'bg-orange-300 hover:bg-orange-200'
  } else if (status === 'ma') {
    return 'bg-yellow-300 hover:bg-yellow-200'
  } else {
    return 'bg-red-300 hover:bg-red-200'
  }


}


const reserve = {}

const open = ref(false)


</script>
    
<template>
  <div class="">
    <div class="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
      <!-- List Lots BEGIN -->
      <div v-if="lots" class="flex flex-wrap -m-4 text-center">
        <a href="#" v-for="{ lot, fare, licence, id, check_in_date, check_in_time, check_in }  in lots" :key="lot.id" class="p-4 w-full md:w-1/2 lg:w-1/3 xl:w-1/4 hover:scale-110"
          @click="open = true, farePrice=fare, licenceNumber=licence, reserve={fare, licence, id, check_in_date, check_in_time, check_in, lot_id:lot.id}">
          <!-- <div class="border-2 border-gray-200  px-4 py-6 rounded-lg hover:shadow-xl hover:absolute -left-6 -top-2 hover:w-full" :class="colorLot(lot.status)"> -->
          <div class="border-2 border-gray-200  px-4 py-6 rounded-lg hover:shadow-xl " :class="colorLot(lot.status)">
            <div class="flex items-center justify-between">
              <h2 class="text-4xl font-bold ">
                {{ lot.name }}
              </h2>
              <svg v-if="lot.type === 'di'" xmlns="http://www.w3.org/2000/svg"
                class="icon icon-tabler icon-tabler-wheelchair animate-pulse" width="24" height="24" viewBox="0 0 24 24"
                stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <circle cx="8" cy="16" r="5"></circle>
                <circle cx="19" cy="19" r="2"></circle>
                <path d="M19 17a3 3 0 0 0 -3 -3h-3.4"></path>
                <path d="M3 3h1a2 2 0 0 1 2 2v6"></path>
                <path d="M6 8h11"></path>
                <path d="M15 8v6"></path>
              </svg>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" class="text-indigo-500 w-12 h-12 mb-3 inline-block animate-bounce "
              fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <circle cx="7" cy="17" r="2"></circle>
              <circle cx="17" cy="17" r="2"></circle>
              <path d="M5 17h-2v-6l2 -5h9l4 5h1a2 2 0 0 1 2 2v4h-2m-4 0h-6m-6 -6h15m-6 0v-5"></path>
            </svg>
            <h2 class="title-font font-medium text-2xl text-gray-900"> {{ licence }}</h2>
          </div>
        </a>
      </div>
      <!-- List Lots END -->

      <!-- charge skeleton BEGIN -->
      <div v-else class="flex flex-wrap space-y-2">
        <div v-for="test in 3" class="w-1/3 bg-white rounded w-96 mx-auto rounded-2xl shadow-lg px-3">
          <div class="bg-gray-200 h-48 p-3 overflow-hidden animate-pulse">
          </div>
          <div class="h- p-3">
            <div class="grid grid-cols-3 gap-4 mt-2">
              <div class="h-8 bg-gray-200 rounded animate-pulse">
              </div>
              <div class="h-8 bg-gray-200 rounded animate-pulse">
              </div>
              <div class="h-8 bg-gray-200 rounded animate-pulse">
              </div>
              <div class="h-8 col-span-2 bg-gray-200 rounded animate-pulse">
              </div>
              <div class=" h-8 bg-gray-200 rounded animate-pulse">
              </div>
              <div class="...">
              </div>
              <div class="col-span-2 ...">
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- charge skeleton END -->
    </div>
  </div>

  <!-- Modal -->
  <Modal :open="open"  @toggle="(value) => open=value" :reserve="reserve" @loadLots="() => loadLots()"/>
</template>
    
    
    