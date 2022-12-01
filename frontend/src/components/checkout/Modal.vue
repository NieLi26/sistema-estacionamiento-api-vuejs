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
            <DialogPanel class="relative inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
              <!-- Title -->
              <DialogTitle class="items-center flex justify-between">
                  <div class="flex items-center">
                      <span
                          class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-green-200 text-white">
                          <PlusIcon class="h-6 w-6" aria-hidden="true" />
                      </span>
                      <p class="text-xl font-bold ml-2 sm:mt-0 sm:ml-3">
                        Nuevo registro de salida
                      </p>
                  </div>

                  <button type="button"
                      class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      @click="setOpen(false)">
                      <span class="sr-only">Close</span>
                      <XIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
              </DialogTitle>
              <!-- Subtitle -->
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
              <div>
                  <div class="mt-6 text-center">
                    <div
                      class="group relative inline-block focus:outline-none focus:ring"
                
                    >
                      <span
                        class="absolute inset-0 translate-x-0 translate-y-0 bg-yellow-300 transition-transform group-hover:translate-y-1.5 group-hover:translate-x-1.5"
                      ></span>

                      <span
                        class="relative inline-block border-2 border-current px-8 py-3 text-xl font-bold uppercase tracking-widest"
                      >
                      {{ clock.time }} {{ clock.ampm }}
                      </span>
                    </div>
                  </div>
                  
                  <div class="mt-6">
                      <div
                          class="py-2 px-4 bg-blue-100 dark:bg-white text-gray-600 border-l-4 border-blue-500 flex items-center">
                          <p class="text-xs flex items-center dark:text-gray-800">
                              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                  stroke="currentColor" class="w-5 h-5 text-blue-500 mr-2">
                                  <path stroke-linecap="round" stroke-linejoin="round"
                                      d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
                              </svg>
                              Resguardado:
                          </p>
                          <div class="flex items-center ">
                              <span class="font-bold text-xs dark:text-gray-800 mr-2 ml-2 md:ml-4">
                                  {{ durationShow }}
                              </span>
                          </div>
                      </div>
                  </div>

                  <div class="mt-6">
                      <div
                          class="py-2 px-4 bg-blue-100 dark:bg-white text-gray-600 border-l-4 border-blue-500 flex items-center">
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

                  <div class="mt-6" v-if="isHidden">
                    <label for="name" class="block text-sm font-medium text-gray-700">Numero Boleta</label>
                    <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                        <input  
                        v-model="formData.number"
                        type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese número boleta">
                        </div>
                  </div> 

                  <div class="mt-6" v-else-if="!isHidden">
                    <label for="name" class="block text-sm font-medium text-gray-700">Observación</label>
                    <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                        <textarea  
                        v-model="formDataReserve.obs"
                        type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese observación"></textarea>
                    </div>
                  </div>   

                  <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                      <button 
                      @click="handleSubmit"
                      type="button"
                          class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"   
                          >
                          Guardar
                      </button>
                      <button type="button"
                          class="mt-3 w-full inline-flex justify-center rounded-md border border-red-300 shadow-sm px-4 py-2 bg-red text-base font-medium text-gray-700 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:mt-0 sm:col-start-1 sm:text-sm"
                          @click="handleCancel"
                          ref="cancelButtonRef">
                          Anular
                      </button>
                  </div>    
              </div>
              <!-- Alert -->
              <div v-if="errors.length" class="mt-5 sm:mt-6 bg-yellow-200 border-yellow-600 text-yellow-600 border-l-4 p-4" role="alert">
                  <p class="font-bold">
                      Error
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
import { XIcon, PlusIcon } from 'vue-tabler-icons';
import CheckOutAPI from '@/services/checkout/CheckOutAPI';
import moment from 'moment-timezone';

watch(() => props.open, () => {

  errors.value = []

  if (!props.open) {
    formData.number = '',
    formData.obs = ''
  }
  
  formDataReserve.lot = props.reserve.lot_id
  let checkInDate = props.reserve.check_in;
  let checkOutDate = moment.tz("America/Santiago").format('MM/DD/YYYY HH:mm');
  checkInDate = moment(checkInDate)
  checkOutDate = moment(checkOutDate);
  duration.value = moment.duration(checkOutDate.diff(checkInDate))
  console.log(formData);
  // console.log(formDataReserve);
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
  console.log(formData);
  errors.value = []

  isHidden.value = true

  let numericTest = /^[0-9]+$/;
  !numericTest.test(formData.number) &&  formData.number !== ''  && errors.value.push('Numero de boleta: Solo deben ser numeros')
  formData.number === '' && errors.value.push('Numero de boleta: No puede estar vacio')


  if (!errors.value.length) {
    CheckOutAPI.createPayment(formData)
      .then(res => {
  
        emit('loadLots')
        setOpen(false);
      })
      .catch(error => {
        if (error.response) {
          for (const property in error.response.data) {
            errors.value.push(`${property}: ${error.response.data[property]}`);
            property === 'reserve' && setOpen(false)
            property === 'reserve' &&  (errors.value = [])
          };

          console.log(JSON.stringify(error.response.data));
          emit('loadLots')
        }
        else if (error.message) {
          errors.value.push('Algo salio mal, porfavor intenta nuevamente')
          console.log(JSON.stringify(error));
        }
      })
  }
}

const isHidden = ref(true)


const formDataReserve = {
  status: 'an',
  obs: '',
  lot: ''
}

const handleCancel = () => {
  errors.value = []

  formDataReserve.obs === '' && errors.value.push('Observación: No puede estar vacia')
  isHidden.value = false


  if (formDataReserve.obs !== '') {
  CheckOutAPI.updateReserve(props.reserve.id, formDataReserve)
    .then(res => {
          console.log(res)
          emit('loadLots')
          setOpen(false);
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              errors.value.push(`${property}: ${error.response.data[property]}`);
              property === 'lot' && setOpen(false)
              property === 'lot' &&  (errors.value = [])
            };

            console.log(JSON.stringify(error.response.data));
            emit('loadLots')
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