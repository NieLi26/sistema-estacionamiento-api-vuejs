<!-- This example requires Tailwind CSS v2.0+ -->
<template>
    <TransitionRoot as="template" :show="isOpen">
        <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto" @close="setOpen(false)">
            <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0"
                    enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                    <DialogOverlay class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                </TransitionChild>

                <!-- This element is to trick the browser into centering the modal contents. -->
                <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
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
                                        {{ props.action === 'create' ? 'Creación de Reserva' : 'Actualización de Reserva'}}
                                    </p>
                                </div>

                                <button type="button"
                                    class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                    @click="setOpen(false)">
                                    <span class="sr-only">Close</span>
                                    <XIcon class="h-6 w-6" aria-hidden="true" />
                                </button>
                        </DialogTitle>

                        <!-- FORM -->
                        <div>

                                             
                            <fieldset class="mt-6" v-if="props.action == 'create'">
                                <legend class="block text-sm font-medium text-gray-700">Estacionamiento</legend>
                                <div class="mt-1 rounded-md shadow-sm -space-y-px">
                                    <div>
                                    <label for="lot" class="sr-only">lot</label>
                                    <select 
                                    v-model="formData.lot"
                                    id="lot" name="lot" autocomplete="lot-name" class="py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 relative block w-full  bg-gray-50 focus:z-10 sm:text-sm border border-gray-300">
                                        <option disabled value=""> ------- </option>
                                        <template v-for="{ name, id, status } in lots" :key="id" >
                                            <option v-if="status === 'av'" :value="id">
                                                {{ name }}
                                            </option>
                                        </template>
                                        
                                    </select>
                                    </div>
                                </div>
                            </fieldset>


                            <fieldset class="mt-6">
                                <legend class="block text-sm font-medium text-gray-700">Tarifa</legend>
                                <div class="mt-1 rounded-md shadow-sm -space-y-px">
                                    <div>
                                    <label for="farePeriod" class="sr-only">fare</label>
                                    <select 
                                    v-model="formData.fare_period"
                                    id="farePeriod" name="farePeriod" autocomplete="farePeriod-name" class="py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 relative block w-full bg-gray-50 focus:z-10 sm:text-sm border border-gray-300">
                                        <option disabled value=""> ------- </option>
                                        <option v-for="{name, id} in faresPeriod" :key="id" :value="id">
                                            {{ name }}
                                        </option>
                                    </select>
                                    </div>
                                </div>
                            </fieldset>

                
                            <!-- <div class="mt-6">
                                <label for="name" class="block text-sm font-medium text-gray-700">Cliente</label>
                                <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                    <input  
                                    v-model="formData.client" 
                                    @keyup="loadClients"
                                    type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese nombre">
                                
                                    <template v-if="clients.length" class="">
                                    <ul class="relative z-10 sm:max-w-lg sm:w-full">
                                        <li v-for="{ first_name, last_name} in clients"  class=" px-4 py-2 border-0 border-b border-transparent bg-gray-300 focus:border-indigo-600 focus:ring-0 sm:text-sm">
                                            <button @click="formData.client = first_name + ' ' + last_name, clients = []">{{ first_name }} {{ last_name }}</button>
                                        </li>
                                    </ul>
                                    </template>
                                </div>
                                
                            </div> -->
               
                            <div class="mt-6">
                                <label for="name" class="block text-sm font-medium text-gray-700">Cliente</label>
                                <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                    <v-select 
                                    class=" focus:ring-indigo-500 focus:border-indigo-500 relative block w-full bg-gray-50 focus:z-10 sm:text-sm border border-gray-300"
                                    v-model="formData.client"  :options="clients" label="first_name" :reduce="first_name => first_name.id"></v-select>
                                </div>
                            </div>
                
                            <div class="mt-6">
                            <label for="name" class="block text-sm font-medium text-gray-700">Patente</label>
                            <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                <input  
                                v-model="formData.licence" 
                                type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese patente">
                            </div>
                            </div>
                
                            <div class="mt-6">
                            <label for="checkin" class="block text-sm font-medium text-gray-700">Fecha Inicio</label>
                            <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                <input  
                                v-model="formData.check_in" 
                                :min='moment.tz("America/Santiago").format("YYYY-MM-DD")'
                                type="date" name="checkin" id="checkin" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese patente">
                            </div>
                            </div>
                
                            <div class="mt-6">
                            <label for="checkout" class="block text-sm font-medium text-gray-700">Fecha Termino</label>
                            <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                <input  
                                v-model="formData.check_out" 
                                :min="formData.check_in"
                                type="date" name="checkout" id="checkout" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese patente">
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
        </Dialog>
    </TransitionRoot>
</template>
  
<script setup>
import { ref, watch } from 'vue'
import { Dialog, DialogOverlay, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XIcon, PlusIcon } from 'vue-tabler-icons';
import FarePeriodAPI from '../../services/FarePeriodAPI';
import ClientAPI from '../../services/ClientAPI';
import ReservePeriodAPI from '../../services/ReservePeriodAPI';
import CheckInAPI from "@/services/checkin/CheckInAPI"; // por mietras debo hacer calls de estacionamientos
import moment from 'moment-timezone';


console.log(moment.tz("America/Santiago").format('MM/DD/YYYY HH:mm'));

watch(() => props.isOpen, () => {

    errors.value = []

    if(props.action === 'update'){
        formData.value.lot = props.reservePeriod.lot
        formData.value.fare_period = props.reservePeriod.fare_period
        formData.value.client = props.reservePeriod.client
        formData.value.licence = props.reservePeriod.licence
        formData.value.check_in = moment(props.reservePeriod.check_in).format('YYYY-MM-DD')
        formData.value.check_out = moment(props.reservePeriod.check_out).format('YYYY-MM-DD')
    }

    if (!props.isOpen) {
        formData.value.lot = ''
        formData.value.fare_period = ''
        formData.value.client = null
        formData.value.licence = ''
        formData.value.check_in = ''
        formData.value.check_out = ''
    }


})

// pasar valor del padre al hijo - en este caso abrir modal
const props = defineProps({
  isOpen: Boolean,
  reservePeriod: Object,
  action: String
})

// console.log(props.reserve);

// pasar valor del hijo al padre - en este caso cerrar el modal
const emit = defineEmits(['toggle', 'loadReservePeriod']);

const setOpen = (value) => {
    // usamos el emit porque el padre debe hacer el cambio de estado, debemos avisarle del cambio, en este caso a false
    emit('toggle', value);
}


const formData = ref({
  lot: '',
  fare_period: '',
  client: null,
  licence: '',
  check_in: '',
  check_out: '',
  total: '',
})



// cargar tarifas
const faresPeriod = ref('')

const loadFaresPeriod = async () => {
  try {
    const response = await FarePeriodAPI.getFaresPeriod();
    faresPeriod.value = response.data;
  } catch (error) {
    console.log(error);
  };
};

loadFaresPeriod();

// cargar estacionamientos
const lots = ref('')

const loadLots = async () => {
  try {
    // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
    const response = await CheckInAPI.getLots();
    // setTimeout(() => {
    lots.value = response.data
    // }, 3000)
  } catch (error) {
    console.log(error);
  }

}

loadLots()


// cargar clientes
const clients = ref([])


const loadClients = async () => {
  try {

    // clients.value = []
    // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
    const response = await ClientAPI.getClients();
    clients.value = response.data
    // if (formData.value.client !== '') {
    //     clients.value = response.data.filter(res => (res.first_name.toLowerCase().includes(formData.value.client.toLowerCase()) || res.last_name.toLowerCase().includes(formData.value.client.toLowerCase())) )
    // }

    // }, 3000)
  } catch (error) {
    console.log(error);
  }

}
loadClients()

// date change restriccion
watch(() => formData.value.check_in, () => {
    if (formData.value.check_in > formData.value.check_out ){
        formData.value.check_out = formData.value.check_in
    }
})


const errors = ref([])

const handleSubmit = () => {
   console.log(formData.value);
    errors.value = []
    formData.value.lot === '' && errors.value.push('Estacionamiento: Debe seleccionar un estacionamiento')
    formData.value.fare_period === '' && errors.value.push('Tarifa: Debe selecionar una tarifa')
    formData.value.client === null  && errors.value.push('Cliente: Debe seleccionar un cliente')
    formData.value.licence === '' && errors.value.push('Patente: No puede estar vacia')
    formData.value.check_in === '' && errors.value.push('Fecha Entrada: Debe seleccionar una fecha')
    formData.value.check_out === '' && errors.value.push('Fecha Salida: Debe seleccionar una fecha')

    // let numericTest = /^[0-9]+$/;
    // !numericTest.test(formData.price.value) &&  formData.price.value !== ''  && errors.value.push('Precio: Solo deben ser numeros')
    // formData.price.value === '' && errors.value.push('No ingreso el precio')

  if (!errors.value.length) {
    let requestMethod = ''

    props.action === 'create' ? requestMethod = ReservePeriodAPI.createReservePeriod(formData.value) : props.action === 'update' ? requestMethod = ReservePeriodAPI.updateReservePeriod(props.reservePeriod.id, formData.value) : requestMethod = FareAPI.deleteFare(props.fare.id)

    requestMethod
      .then(res => {
        console.log(res)
        emit('loadReservePeriod');
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
          emit('loadReservePeriod');
        }
        else if (error.message) {
          errors.value.push('Algo salio mal, porfavor intenta nuevamente')
          console.log(JSON.stringify(error));
        }
      })
  }
}


</script>