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
            <DialogPanel
        class="inline-block p-5 overflow-hidden text-left align-bottom transition-all transform bg-white dark:bg-gray-800 rounded-lg shadow-2xl lg:p-8 sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
              <!-- Title -->
              <DialogTitle class="flex items-center justify-between">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-600" width="24" height="24"
                      viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"
                      stroke-linejoin="round">
                      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                      <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                      <path d="M9 16v-8h4a2 2 0 0 1 0 4h-4"></path>
                  </svg>
                  <h1 class=" text-2xl font-extrabold leading-none tracking-tighter text-gray-800 dark:text-white"> Nuevo
                      registro de salida</h1>
                  <span @click="setOpen(false)" class="cursor-pointer">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                          <path fill-rule="evenodd"
                              d="M5.47 5.47a.75.75 0 011.06 0L12 10.94l5.47-5.47a.75.75 0 111.06 1.06L13.06 12l5.47 5.47a.75.75 0 11-1.06 1.06L12 13.06l-5.47 5.47a.75.75 0 01-1.06-1.06L10.94 12 5.47 6.53a.75.75 0 010-1.06z"
                              clip-rule="evenodd" />
                      </svg>
                  </span>
              </DialogTitle>
              <div class="bg-blue-50 border border-blue-400 rounded text-blue-800 text-sm p-4 flex items-start mt-4">
                  <div>
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" viewBox="0 0 20 20" fill="currentColor">
                          <path fill-rule="evenodd"
                              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                              clip-rule="evenodd" />
                      </svg>
                  </div>
                  <div class="w-full">
                      <p>
                          <span class="font-bold uppercase">Info!</span>
                          <br>
                      <p class="text-blue-600">
                          Numero patente: <b class="uppercase">{{ props.reserve.licence }}</b><br>
                          Valor por minuto: <b>${{ props.reserve.fare.price }} pesos</b> <br>
                          Valor Base: <b>$500 pesos hasta los 30 min</b>
                      </p>
                      </p>
                  </div>
              </div>
              <!-- Form -->
              <form @submit.prevent="handleSubmit" id="revue-form" name="revue-form" target="_blank" class="">
                  <div class="container items-center px-5 py-12 lg:px-8 mx-auto space-y-4">
                      <div class="relative">
                          <p class="font-bold text-xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce"> {{
                          clock.date }}</p>
                          <h3 id="clock"
                              class="font-bold text-2xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce">
                              {{ clock.time }} {{ clock.ampm }}
                          </h3>
                      </div>
                      <div class="relative">
                          <div
                              class="py-2 px-4 bg-blue-100 dark:bg-white text-gray-600 border-l-4 border-blue-500 flex items-center justify-between">
                              <p class="text-xs flex items-center dark:text-gray-800">
                                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                      stroke="currentColor" class="w-5 h-5 text-blue-500 mr-2">
                                      <path stroke-linecap="round" stroke-linejoin="round"
                                          d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                                  </svg>
                                  Resguardado:
                              </p>
                              <div class="flex items-center">
                                  <span class="font-bold text-xs dark:text-gray-800 mr-2 ml-2 md:ml-4">
                                      {{ durationShow }}
                                  </span>
                                  <!-- <button class="text-sm p-1 text-gray-400 border rounded bg-blue-500 mr-4">
                                      <svg width="17" height="17" fill="currentColor" viewBox="0 0 24 24" class="text-white">
                                        <g fill="none">
                                          <path
                                            d="M9 6a1 1 0 0 1 1 1v10a1 1 0 1 1-2 0V7a1 1 0 0 1 1-1zm6 0a1 1 0 0 1 1 1v10a1 1 0 1 1-2 0V7a1 1 0 0 1 1-1z"
                                            fill="currentColor">
                                          </path>
                                        </g>
                                      </svg>
                                    </button> -->
                              </div>
                          </div>
                      </div>
                      <div class="relative">
                          <div
                              class="py-2 px-4 bg-blue-100 dark:bg-white text-gray-600 border-l-4 border-blue-500 flex items-center justify-between">
                              <p class="text-xs flex items-center dark:text-gray-800">
                                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                      stroke="currentColor" class="w-5 h-5 text-blue-500 mr-2">
                                      <path stroke-linecap="round" stroke-linejoin="round"
                                          d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                  </svg>
                                  Valor Total:
                              </p>
                              <div class="flex items-center">
                                  <span class="font-bold text-xs dark:text-gray-800 mr-2 ml-2 md:ml-4">
                                      $ {{ total }}
                                  </span>
                              </div>
                          </div>
                      </div>
                      <div class="relative" v-if="isHidden">
                          <label for="name" class="text-base leading-7 text-blueGray-500">Numero Boleta</label>
                          <input type="numeric" id="name" v-model="formData.number"
                              class="w-full px-4 py-2 mt-2 mr-4 text-base text-black transition duration-500 ease-in-out transform rounded-lg bg-gray-100 focus:border-blueGray-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2">
                      </div>
                      <div class="relative" v-if="!isHidden">
                          <label for="name" class="text-base leading-7 text-blueGray-500">Observación</label>
                          <textarea v-model="formData.obs" name="" id="" cols="30" rows="5"
                              class="w-full px-4 py-2 mt-2 mr-4 text-base text-black transition duration-500 ease-in-out transform rounded-lg bg-gray-100 focus:border-blueGray-500 focus:bg-white focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2"></textarea>
                      </div>
                  </div>
                  <div class="flex items-center w-full pt-4 mb-4 space-x-2">
                      <button
                          class="w-full py-3 text-base text-white transition duration-500 ease-in-out transform bg-blue-600 border-blue-600 rounded-md focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2 hover:bg-blue-800 ">
                          Registrar Salida
                      </button>
                      <button @click="handleCancel" type="button"
                          class="w-full py-3 text-base text-white transition duration-500 ease-in-out transform bg-red-600 border-red-600 rounded-md focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2 hover:bg-red-800 ">
                          Anular
                      </button>
                  </div>
              </form>
              <!-- Alert -->
              <div v-if="errors.length" class="bg-yellow-200 border-yellow-600 text-yellow-600 border-l-4 p-4" role="alert">
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
import { onBeforeMount, onMounted, ref, watch } from 'vue'
import { Dialog, DialogPanel, DialogTitle, DialogDescription, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'
import CheckOutAPI from '@/services/checkout/CheckOutAPI';
import moment from 'moment-timezone';

watch(() => props.open, () => {

  errors.value = []

  if (!props.open) {
    formData.number = '',
    formData.obs = ''
  }

  let checkInDate = props.reserve.check_in;
  let checkOutDate = moment.tz("America/Santiago").format('MM/DD/YYYY HH:mm');
  checkInDate = moment(checkInDate)
  checkOutDate = moment(checkOutDate);

  duration.value = moment.duration(checkOutDate.diff(checkInDate))

  // duration.value.difference.asMinutes() > 1 && (duration.value.minutes = Math.trunc(duration.value.difference.asMinutes()))
  // duration.value.difference.asHours() > 1 && (duration.value.hours = Math.trunc(duration.value.difference.asHours()))
  // duration.value.difference.asDays() > 1 && (duration.value.days = Math.trunc(duration.value.difference.asDays()))

  //Get Days and subtract from duration
  // var days = Math.floor(duration.value.days());
  // duration.value.subtract(moment.duration(days,'days'));

  //Get hours and subtract from duration
  var hours = duration.value.hours();
  // duration.value.subtract(moment.duration(hours,'hours'));

  //Get Minutes and subtract from duration
  var minutes = duration.value.minutes();
  // duration.value.subtract(moment.duration(minutes,'minutes'));


  // durationShow.value = `${days} dias,  ${hours} horas y ${minutes} minutos`
  durationShow.value = `${hours} horas y ${minutes} minutos`


  // Valorminutes total
  Math.floor(duration.value.asMinutes())<= 30 ? total.value = 500 : total.value = (props.reserve.fare.price * (Math.floor(duration.value.asMinutes())-30)) + 500;
  
  // CheckOutAPI.getReserve(props.reserve.id)
  //             .then(res => formData.reserve = res.data)
})

// forma 1 abriendo desde el mismo componente
// const open = ref(false)

// const setOpen = (value) => {
//   open.value = value
// }



// forma 2 maninupalcion desde el padre
const props = defineProps({
  open: Boolean,
  reserve: Object
})

const emit = defineEmits(['toggle', 'loadLots']);


const setOpen = (value) => {
  // usamos el emit porque el padre debe hacer el cambio de estado
  emit('toggle', value);
}


// valor total
const total = ref(0)

let formData = {
  reserve: '',
  number: '',
  total: 0,
  obs: '',
}


const errors = ref([])

const handleSubmit = () => {

  formData.reserve = props.reserve.id
  formData.total = total.value

  errors.value = []

  isHidden.value = true

  let numericTest = /[0-9]$/;
  !numericTest.test(formData.number) &&  formData.number !== ''  && errors.value.push('Numero de boleta: Solo deben ser numeros')
  formData.number === '' && errors.value.push('Numero de boleta: No puede estar vacio')


  if (!errors.value.length) {
    CheckOutAPI.createPayment(formData)
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

const isHidden = ref(true)

const handleCancel = () => {
  errors.value = []

  formData.obs === '' && errors.value.push('Observación: No puede estar vacia')
  isHidden.value = false


  if (formData.obs !== '') {
  CheckOutAPI.updateReserve(props.reserve.id, {status: 'an', obs: formData.obs})
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


// diferencai tiempo
const durationShow = ref('')

const duration = ref('')

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