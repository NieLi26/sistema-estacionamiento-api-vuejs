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
                    <div
                        class="relative inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6">
                        <div>
                            <div class="items-center flex justify-between">
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
                            </div>

                                             
                            <fieldset class="mt-6">
                                <legend class="block text-sm font-medium text-gray-700">Estacionamiento</legend>
                                <div class="mt-1 rounded-md shadow-sm -space-y-px">
                                    <div>
                                    <label for="lot" class="sr-only">Country</label>
                                    <select id="lot" name="lot" autocomplete="lot-name" class="py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 relative block w-full  bg-gray-50 focus:z-10 sm:text-sm border border-gray-300">
                                        <option selected> ------- </option>
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
                                    <label for="farePeriod" class="sr-only">Country</label>
                                    <select id="farePeriod" name="farePeriod" autocomplete="farePeriod-name" class="py-2 px-4 focus:ring-indigo-500 focus:border-indigo-500 relative block w-full bg-gray-50 focus:z-10 sm:text-sm border border-gray-300">
                                        <option selected> ------- </option>
                                        <option v-for="{name, id} in faresPëriod" :key="id" :value="id">
                                            {{ name }}
                                        </option>
                                    </select>
                                    </div>
                                </div>
                            </fieldset>

                
                            <div class="mt-6">
                                <label for="name" class="block text-sm font-medium text-gray-700">Cliente</label>
                                <div class="mt-1 border-b border-gray-300 focus-within:border-indigo-600">
                                    <input  
                                    v-model="formData.client" 
                                    @keyup="loadClients"
                                    type="text" name="name" id="name" class="px-4 py-2 block w-full border-0 border-b border-transparent bg-gray-50 focus:border-indigo-600 focus:ring-0 sm:text-sm" placeholder="Ingrese nombre">
                                
                                    <template v-if="clients.length">
                                    <ul class="absolute z-10 w-full ">
                                        <li v-for="{ first_name, last_name} in clients"  class="px-4 py-2 border-0 border-b border-transparent bg-gray-300 focus:border-indigo-600 focus:ring-0 sm:text-sm">
                                            <button @click="formData.client = first_name + ' ' + last_name, clients = []">{{ first_name }} {{ last_name }}</button>
                                        </li>
                                    </ul>
                                    </template>
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
                
                       
                        </div>
                        <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                            <button type="button"
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

                        <!-- Alert -->
                        <!-- <div v-if="errors.length" class="mt-5 sm:mt-6 bg-yellow-200 border-yellow-600 text-yellow-600 border-l-4 p-4" role="alert">
                            <p class="font-bold">
                                Error
                            </p>
                            <p v-for="error in errors" :key="error">
                                {{ error }}
                            </p>
                        </div> -->
                    </div>
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
import CheckInAPI from "@/services/checkin/CheckInAPI"; // por mietras debo hacer calls de estacionamientos
import moment from 'moment-timezone';


console.log(moment.tz("America/Santiago").format('MM/DD/YYYY HH:mm'));
// watch(() => props.isOpen, () => {

//     errors.value = []

//     formData.name = props.fare.name
//     formData.price = props.fare.price

//     if (!props.isOpen) {
//         formData.name = ''
//         formData.price = ''
//     }


// })

// pasar valor del padre al hijo - en este caso abrir modal
const props = defineProps({
  isOpen: Boolean,
//   fare: Object,
//   action: String
})

// console.log(props.reserve);

// pasar valor del hijo al padre - en este caso cerrar el modal
const emit = defineEmits(['toggle', 'loadFares']);

const setOpen = (value) => {
    // usamos el emit porque el padre debe hacer el cambio de estado, debemos avisarle del cambio, en este caso a false
    emit('toggle', value);
}


const formData = ref({
  name: '',
  price: '',
  client: '',
  check_in: '',
  check_out: ''
})



// cargar tarifas
const faresPëriod = ref('')

const loadFaresPeriod = async () => {
  try {
    const response = await FarePeriodAPI.getFaresPeriod();
    faresPëriod.value = response.data;
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

    clients.value = []
    // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
    const response = await ClientAPI.getClients();

    if (formData.value.client !== '') {
        clients.value = response.data.filter(res => (res.first_name.toLowerCase().includes(formData.value.client.toLowerCase()) || res.last_name.toLowerCase().includes(formData.value.client.toLowerCase())) )
    }

    // }, 3000)
  } catch (error) {
    console.log(error);
  }

}

// date change restriccion
watch(() => formData.value.check_in, () => {
    if (formData.value.check_in > formData.value.check_out ){
        formData.value.check_out = formData.value.check_in
    }
})


// const changeData = () => {
//     formData.client = 'feo' 
// }

// const getClient = () => return 



// const errors = ref([])

// const handleSubmit = () => {
//     errors.value = []
//     formData.name === '' && errors.value.push('No ingreso el nombre')
//     formData.price === '' && errors.value.push('No ingreso el precio')

//     let numericTest = /[0-9]$/;
//     !numericTest.test(formData.price) &&  formData.price !== ''  && errors.value.push('Precio: Solo deben ser numeros')

//   if (!errors.value.length) {
//     let requestMethod = ''

//     props.action === 'create' ? requestMethod = FareAPI.createFare(formData) : props.action === 'update' ? requestMethod = FareAPI.updateFare(props.fare.id, formData) : requestMethod = FareAPI.deleteFare(props.fare.id)

//     requestMethod
//       .then(res => {
//         console.log(res)
//         emit('loadFares');
//         setOpen(false);
//       })
//       .catch(error => {
//         if (error.response) {
//           for (const property in error.response.data) {
//             errors.value.push(`${property}: ${error.response.data[property]}`);
//           };

//           console.log(JSON.stringify(error.response.data));
//         }
//         else if (error.message) {
//           errors.value.push('Algo salio mal, porfavor intenta nuevamente')
//           console.log(JSON.stringify(error));
//         }
//       })
//   }
// }


</script>