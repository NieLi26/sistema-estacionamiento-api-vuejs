<!-- This example requires Tailwind CSS v2.0+ -->
<template>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="sm:flex sm:items-center">
        <div class="sm:flex-auto">
          <h1 class="text-xl font-semibold text-gray-900">Transactions</h1>
          <p class="mt-2 text-sm text-gray-700">A table of placeholder stock market data that does not make any sense.</p>
        </div>
        <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
          <button
          @click="isOpen = true"
           type="button" class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto">Agregar</button>
        </div>
      </div>
      <div class="mt-8 flex flex-col">
        <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
            <div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
              <table class="min-w-full divide-y divide-gray-300">
                <thead class="bg-gray-50">
                  <tr>
                    <th scope="col" class="whitespace-nowrap py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">ID</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Fecha Inicio</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Fecha Termino</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Patente</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-sm font-semibold text-gray-900">Estacionamiento</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Tarifa</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Total</th>
                    <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Estado</th>
                    <th scope="col" class="relative whitespace-nowrap py-3.5 pl-3 pr-4 sm:pr-6">
                      <span class="sr-only">Edit</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 bg-white">
                  <tr v-for="{ id, lot, check_in, check_out, licence, fare_period, total } in reservePeriod" :key="id">
                    <td class="whitespace-nowrap py-2 pl-4 pr-3 text-sm text-gray-500 sm:pl-6">{{ id }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-sm font-medium text-gray-900"> {{  check_in ? moment(check_in).format('l') : 'No existe registro' }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-sm font-medium text-gray-900"> {{  check_out ? moment(check_out).format('l') : 'No existe registro' }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-900">{{ licence }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-center text-sm text-gray-500">{{ lot }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-500">{{ fare_period }}</td>
                    <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-500">${{ total }}</td>
                    <td class="relative whitespace-nowrap py-2 pl-3 pr-4  text-sm font-medium sm:pr-6">
                      <a href="#" class="text-indigo-600 hover:text-indigo-900"
                        >Edit<span class="sr-only"> </span></a
                      >
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Modal :isOpen="isOpen" @toggle="(value) => isOpen=value" />
  </template>
  
  <script setup>
import { ref } from "vue";
import ReservePeriodAPI from "@/services/ReservePeriodAPI"
import moment from 'moment/min/moment-with-locales';
import Modal from '../components/reserves_period/Modal.vue';

  
  moment.locale('es'); // default the locale to Spanish

  const reservePeriod = ref('')

  const loadReservePeriod = async () => {
    try {
        // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
        const response = await ReservePeriodAPI.getReservePeriods();
        // setTimeout(() => {
          reservePeriod.value = response.data;
        // }, 3000)
    } catch (error) {
        console.log(error);
    }

}

loadReservePeriod();

// data enviada a modal
const isOpen = ref(false)

  </script>