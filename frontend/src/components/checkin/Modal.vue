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
            <DialogPanel class="relative inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6"> 
              <!-- Title -->
              <DialogTitle class="items-center flex justify-between">
                  <div class="flex items-center">
                      <span
                          class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-green-200 text-white">
                          <PlusIcon class="h-6 w-6" aria-hidden="true" />
                      </span>
                      <p class="text-xl font-bold ml-2 sm:mt-0 sm:ml-3">
                        Nuevo registro de reserva
                      </p>
                  </div>

                  <button type="button"
                      class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                      @click="setOpen(false)">
                      <span class="sr-only">Close</span>
                      <XIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
              </DialogTitle>
             <!-- Form -->
              <div>
            
                  <!-- <div class="mt-6">
                      <p class="font-bold text-xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce"> {{ clock.date }}</p>
                      <h3 id="clock" class="font-bold text-2xl dark:text-gray-200 mr-2 ml-2 md:ml-4 text-center animate-bounce">
                      {{ clock.time }} {{ clock.ampm }}
                      </h3>
                  </div> -->
                  <!-- <div class="mt-6">
                    <div
                      class="flex items-center justify-center text-xl rounded-xl border-4 border-black bg-pink-100 px-8 py-4 font-bold shadow-[6px_6px_0_0_#000] transition hover:shadow-none focus:outline-none focus:ring active:bg-pink-50"      
                    >
                    {{ clock.time }} {{ clock.ampm }}
                    </div>

                  </div> -->
                  <div class="mt-6 text-center">
                    <!-- Hover -->

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
              
                  <fieldset class="mt-6">
                      <legend class="block text-sm font-medium text-gray-700">Tarifa</legend>
                      <div class="mt-1 rounded-md shadow-sm -space-y-px">
                          <div>
                          <label for="fare" class="sr-only">fare</label>
                          <select 
                          v-model="formData.fare"
                          id="fare" name="fare" autocomplete="fare-name" class="py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 relative block w-full bg-gray-50 focus:z-10 sm:text-sm border border-gray-300">
                              <option disabled value=""> ------- </option>
                              <option v-for="option in fares" :key="option.id" :value="option.id" >{{ option.name }}</option>
                          </select>
                          </div>
                      </div>
                  </fieldset>

                  <div class="mt-6">
                        <label for="name" class="block text-sm font-medium text-gray-700">Patente</label>
                        <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                            <input  
                            v-model="formData.licence" 
                            type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese patente">
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
                          class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm"
                          @click="setOpen(false)" ref="cancelButtonRef">
                          Cancel
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
import { ref, watch } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XIcon, PlusIcon } from 'vue-tabler-icons';
import FareAPI from '@/services/FareAPI';
import CheckInAPI from '@/services/checkin/CheckInAPI';

// watch(() => testProp.lotNumber, () => {
//   testProp.lotNumber

// })

// const open = ref(testProp.lotNumber)

watch(() => props.open, () => {

  errors.value = []

  if (!props.open) {
    formData.fare = '',
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
  fare: '',
  licence: '',
  lot: ''
}


const errors = ref([])

const handleSubmit = () => {
  errors.value = []
  formData.fare === '' && errors.value.push('Tarifa: Debe selecionar una tarifa')
  formData.licence === '' && errors.value.push('Patente: No ingreso la patente')
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
            errors.value.push(`${property}: ${error.response.data[property]}`); // lo ideal mostrarlo en un alert
            property === 'lot' && setOpen(false)
            property === 'lot' &&  (errors.value = [])
          };

          console.log(JSON.stringify(error.response.data));
          emit('loadLots')
          // setOpen(false);
        }
        else if (error.message) {
          errors.value.push('Algo salio mal, porfavor intenta nuevamente')
          console.log(JSON.stringify(error));
        }
      })
  }
}

// Carga de Tarifas
const fares = ref([])


const loadFares = async () => {
  try {
    const response = await FareAPI.getFares();
    console.log(response.data);
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