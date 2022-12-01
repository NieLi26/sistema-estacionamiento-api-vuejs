<template>
<!-- This example requires Tailwind CSS v2.0+ -->
<div class="px-4 sm:px-6 lg:px-8">
  <div class="sm:flex sm:items-center sm:justify-end">
    <div class="mt-4 sm:mt-0 sm:ml-16 ">
      <button 
      @click="isOpen = true, dataFare = {name: '', price: ''}, action = 'create'"
      type="button" class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto">Agregar</button>
    </div>
  </div>
  <div class="mt-8 flex flex-col">
    <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
        <div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
          <table class="min-w-full divide-y divide-gray-300">
            <thead class="bg-gray-50">
              <tr class="divide-x divide-gray-200">
                <th scope="col" class="py-3.5 pl-4 pr-4 text-left text-sm font-semibold text-gray-900 sm:pl-6">Id</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Nombre</th>
                <th scope="col" class="px-4 py-3.5 text-left text-sm font-semibold text-gray-900">Precio</th>
                <th scope="col" class="px-4  py-3.5 text-sm font-semibold text-gray-900">Acciones</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              <tr v-for="{id, name, price} in fares" :key="id" class="divide-x divide-gray-200">
                <td class="whitespace-nowrap py-4 pl-4 pr-4 text-sm font-medium text-gray-900 sm:pl-6">{{ id }}</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">{{ name }}</td>
                <td class="whitespace-nowrap p-4 text-sm text-gray-500">{{ price }}</td>
                <td class="whitespace-nowrap py-4 text-sm text-gray-500 ">
                  <div class="flex items-center justify-center -space-x-4 hover:space-x-1">
                    <!-- <button
                      class="z-10 block rounded-full border-2 border-white bg-green-100 p-4 text-green-700 transition-all hover:scale-110 focus:outline-none focus:ring active:bg-green-50"
                      type="button"
                    >
                      <svg
                        class="h-4 w-4"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                        />
                      </svg>
                    </button> -->

                    <button
                    @click="isOpen = true, dataFare = {name: name, price: price, id: id}, action = 'update'"
                      class="z-10 block rounded-full border-2 border-white bg-blue-100 p-4 text-blue-700 transition-all hover:scale-110 focus:outline-none focus:ring active:bg-blue-50"
                      type="button"
                    >
                      <svg
                        class="h-4 w-4"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                        />
                      </svg>
                    </button>

                    <button
                    
                      @click="isOpenCancel = true, dataFare = {name: '', price: '', id: id}"
                      class="z-10 block rounded-full border-2 border-white bg-red-100 p-4 text-red-700 transition-all hover:scale-110 focus:outline-none focus:ring active:bg-red-50"
                      type="button"
                    >
                      <svg
                        class="h-4 w-4"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                        />
                      </svg>
                    </button>
                  </div>
                </td>
              </tr>
              <!-- More people... -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <nav class="border-t border-gray-200 px-4 flex items-center justify-between sm:px-0">
    <div class="-mt-px w-0 flex-1 flex">
      <button
      v-if="showPreviousButton"
      @click="loadPrevious"
      class="border-t-2 border-transparent pt-4 pr-1 inline-flex items-center text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
        <ArrowNarrowLeftIcon class="mr-3 h-5 w-5 text-gray-400" aria-hidden="true" />
        Previous
      </button>
    </div>
    <div class="hidden md:-mt-px md:flex">
      <a href="#" class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> 1 </a>
      <!-- Current: "border-indigo-500 text-indigo-600", Default: "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300" -->
      <a href="#" class="border-indigo-500 text-indigo-600 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium" aria-current="page"> 2 </a>
      <a href="#" class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> 3 </a>
      <span class="border-transparent text-gray-500 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> ... </span>
      <a href="#" class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> 8 </a>
      <a href="#" class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> 9 </a>
      <a href="#" class="border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 border-t-2 pt-4 px-4 inline-flex items-center text-sm font-medium"> 10 </a>
    </div>
    <div class="-mt-px w-0 flex-1 flex justify-end">
      <button 
      v-if="showNextButton"
      @click="loadNext"
      class="border-t-2 border-transparent pt-4 pl-1 inline-flex items-center text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300">
        Next
        <ArrowNarrowRightIcon class="ml-3 h-5 w-5 text-gray-400" aria-hidden="true" />
      </button>
    </div>
  </nav>

</div>

<Modal :isOpen="isOpen" :fare="dataFare" :action="action" @toggle="(value) => isOpen = value"  @loadFares="() => loadFares()"/>
<ModalDelete :isOpen="isOpenCancel" :fare="dataFare" @toggle="(value) => isOpenCancel = value" @loadFares="() => loadFares()"/>
</template>

<script setup>
// import { ArrowNarrowLeftIcon, ArrowNarrowRightIcon } from '@heroicons/vue/24/solid'
import { ArrowNarrowLeftIcon, ArrowNarrowRightIcon } from 'vue-tabler-icons';
import FareAPI from "@/services/FareAPI"
import { ref } from "vue";
import Modal from "../components/tarif/Modal.vue";
import ModalDelete from "../components/tarif/ModalDelete.vue";


// PAGINATOR
const currentPage = ref(1)
const showNextButton = ref(false)
const showPreviousButton = ref(false)

const loadNext = () => {
    currentPage.value++
    loadFares();
}

const loadPrevious = () => {
    currentPage.value--
    loadFares();
}


// Cargar todas las tarifas
const fares = ref('')

const loadFares = async () => {
    try {
        const response = await FareAPI.getFaresPaginator(currentPage.value);
        // setTimeout(() => {
          showNextButton.value = false
          showPreviousButton.value = false

          if(response.data.next){
            showNextButton.value = true
          }

          if(response.data.previous){
            showPreviousButton.value = true
          }

        fares.value = response.data.results;
        // }, 3000)
    } catch (error) {
        console.log(error);
    }
};

loadFares();


// data enviada a modal
const isOpen = ref(false)

const isOpenCancel = ref(false)

const action = ref('')

const dataFare = ref({
  id: null,
  name: '',
  price: ''
})




</script>