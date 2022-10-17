<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Orbitron');
  /* *{
    color: black;
    user-select: none;
    background-color: rgb(241, 225, 6);
    font-family: 'Orbitron';
  } */

  
  #clock {
    font-family: 'Orbitron';
  
  }
  
</style>

<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <!-- <button type="button" @click="setOpen(true)"
    class="rounded-md bg-black bg-opacity-20 px-4 py-2 text-sm font-medium text-white hover:bg-opacity-30 focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75">
    Open dialog
  </button> -->

  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="setOpen(false)">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel class="inline-block p-5 overflow-hidden text-left align-bottom transition-all transform bg-white dark:bg-gray-800 rounded-lg shadow-2xl lg:p-8 sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"> 
              <!-- Title -->
              <DialogTitle class="flex items-center justify-between">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-600" width="24" height="24"
                            viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                            stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                            <path d="M9 16v-8h4a2 2 0 0 1 0 4h-4"></path>
                  </svg>
                  <h1 class=" text-2xl font-extrabold leading-none tracking-tighter text-gray-800 dark:text-white"> Nuevo registro de reserva</h1>
                  <span @click="setOpen(false)" class="cursor-pointer">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                            <path fill-rule="evenodd" d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z" clip-rule="evenodd" />
                          </svg>
                  </span>
              </DialogTitle>
             <!-- Form -->
              <form @submit.prevent="handleSubmit" id="revue-form" name="revue-form" target="_blank" class="">
                  <div class="container items-center px-5 py-12 lg:px-8 mx-auto space-y-4">
                  <div class="relative">
                      <p class="font-bold text-xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce"> {{ clock.date }}</p>
                      <h3 id="clock" class="font-bold text-2xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce">
                      {{ clock.time }} {{ clock.ampm }}
                      </h3>
                  </div>
                  <div class="relative">
                      <label for="name" class="text-base leading-7 text-blueGray-500">Tarifa</label>
                      <select id="name" v-model="formData.fare"
                      class="w-full px-4 py-2 mt-2 text-base text-black transition duration-500 ease-in-out transform rounded-lg bg-gray-100 focus:border-blueGray-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2">
                      <!-- <option selected> ------- </option> -->
                      <option v-for="option in fares" :key="option.id" :value="option.id"
                          :selected="option === formData.fare">{{ option.name }}</option>
                      </select>
                  </div>
                  <div class="relative">
                      <label for="name" class="text-base leading-7 text-blueGray-500">Patente</label>
                      <input type="text" id="name" v-model="formData.licence"
                      class="uppercase w-full px-4 py-2 mt-2 mr-4 text-base text-black transition duration-500 ease-in-out transform rounded-lg bg-gray-100 focus:border-blueGray-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2">
                  </div>
                  </div>
                  <div class="flex items-center w-full pt-4 mb-4">
                  <button
                      class="w-full py-3 text-base text-white transition duration-500 ease-in-out transform bg-blue-600 border-blue-600 rounded-md focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2 hover:bg-blue-800 ">
                      Button </button>
                  </div>
              </form>
              <!-- Alert -->
              <div v-if="errors.length" class="bg-yellow-200 border-yellow-600 text-yellow-600 border-l-4 p-4"
                  role="alert">
                  <p class="font-bold">
                  Danger
                  </p>
                  <p v-for="error in errors" :key="error">
                  {{ error }}
                  </p>
              </div>

            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>
  
<script setup>
import { ref, watch } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'
import FareAPI from '@/services/FareAPI';
import CheckInAPI from '@/services/checkin/CheckInAPI';

// watch(() => testProp.lotNumber, () => {
//   testProp.lotNumber

// })

// const open = ref(testProp.lotNumber)

watch(() => props.open, () => {

  if (!props.open) {
    formData.fare = 1,
    formData.licence = ''
  }


})
// forma 1 abriendo desde el mismo componente
// const open = ref(false)

// const setOpen = (value) => {
//   open.value = value
// }



// forma 2 maninupalcion desde el padre
const props = defineProps({
  open: Boolean,
  lotNumber: Number
})

const emit = defineEmits(['toggle', 'loadLots']);


const setOpen = (value) => {
  // usamos el emit porque el padre debe hacer el cambio de estado
  emit('toggle', value);
}


let formData = {
  fare: 1,
  licence: '',
  lot: ''
}


const errors = ref([])

const handleSubmit = () => {
  errors.value = []
  formData.licence === '' && errors.value.push('No ingreso la patente')
  formData.lot = props.lotNumber

  if (!errors.value.length) {
    CheckInAPI.createReserve(formData)
      .then(res => {
        console.log(res)
        emit('loadLots')
        setOpen(false);
      })
      .catch(error => {
        if (error.response) {
          for (const property in error.response.data) {
            errors.value.push(`${property}: ${error.response.data[property]}`);
          };

          console.log(JSON.stringify(error.response.data));
        }
        else if (error.message) {
          errors.value.push('Algo salio mal, porfavor intenta nuevamente')
          console.log(JSON.stringify(error));
        }
      })
  }
}


const fares = ref('')


const loadFares = async () => {
  try {
    const response = await FareAPI.getFares();
    fares.value = response.data;
  } catch (error) {
    console.log(error);
  };
};

loadFares();


// Reloj 
const clock = ref({
  time: '',
  date: '',
  ampm: ''
})


setInterval(() => {
  const date = new Date();
  const week = ['DOMINGO', 'LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SABADO'];
  const month = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'];
  let w = week[date.getDay()]
  let m = month[date.getMonth()]
  clock.value.ampm = date.getHours() >= 12 ? 'PM' : 'AM';
  clock.value.time = ("0" + date.getHours()).slice(-2) + ":" + ("0" + date.getMinutes()).slice(-2) + ":" + ("0" + date.getSeconds()).slice(-2);
  clock.value.date = `${w} ${date.getDate()} de ${m} de ${date.getFullYear()}`.toLowerCase()

}, 1000)


</script>