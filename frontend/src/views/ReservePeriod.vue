<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <fieldset class="w-full space-y-1 dark:text-gray-100">
          <label for="Search" class="hidden">Search</label>
          <div class="relative">
            <span class="absolute inset-y-0 left-0 flex items-center pl-2">
              <button type="button" title="search" class="p-1 focus:outline-none focus:ring">
                <svg fill="currentColor" viewBox="0 0 512 512" class="w-4 h-4 dark:text-gray-100">
                  <path
                    d="M479.6,399.716l-81.084-81.084-62.368-25.767A175.014,175.014,0,0,0,368,192c0-97.047-78.953-176-176-176S16,94.953,16,192,94.953,368,192,368a175.034,175.034,0,0,0,101.619-32.377l25.7,62.2L400.4,478.911a56,56,0,1,0,79.2-79.195ZM48,192c0-79.4,64.6-144,144-144s144,64.6,144,144S271.4,336,192,336,48,271.4,48,192ZM456.971,456.284a24.028,24.028,0,0,1-33.942,0l-76.572-76.572-23.894-57.835L380.4,345.771l76.573,76.572A24.028,24.028,0,0,1,456.971,456.284Z">
                  </path>
                </svg>
              </button>
            </span>
            <input @keyup="currentPage=1, loadReservePeriod()" v-model='q' type="search" name="Search" placeholder="Search..."
              class="w-64 py-2 pl-10 text-sm rounded-md sm:w-full focus:outline-none dark:bg-gray-800 dark:text-gray-100 focus:dark:bg-gray-900 focus:dark:border-violet-400">
          </div>
        </fieldset>
      </div>
      <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
        <button
          @click="isOpen = true, action = 'create', dataReservePeriod = { check_in: '', check_out: '', fare_period: '', lot: '' }"
          type="button"
          class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto">Agregar</button>
      </div>
    </div>
    <div class="mt-8 flex flex-col">
      <div class="-my-2 -mx-4 sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div class="shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
            <table class="min-w-full divide-y divide-gray-300">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col"
                    class="whitespace-nowrap py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">ID
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Fecha Inicio
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Fecha Termino
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Cantidad Dias
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Patente
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-sm font-semibold text-gray-900">
                    Estacionamiento
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Tarifa
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
                    Total
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-sm font-semibold text-gray-900">
                    Estado
                  </th>
                  <th scope="col" class="whitespace-nowrap px-2 py-3.5 text-sm font-semibold text-gray-900">
                    Acciones
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 bg-white" >
                <tr v-for="{ id, client, lot, check_in, check_out, licence, fare_period, total, status } in reservePeriod" :key="id">
                  <td class="whitespace-nowrap py-2 pl-4 pr-3 text-sm text-gray-500 sm:pl-6">{{ id }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm font-medium text-gray-900"> {{ check_in ? moment(check_in).format('l') : 'No existe registro'}}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm font-medium text-gray-900"> {{ check_out ? moment(check_out).format('l') : 'No existe registro' }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-center text-sm font-medium text-gray-900"> {{ check_in && check_out ? moment(check_out).diff(moment(check_in), 'days') : 'No existe registro' }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-900">{{ licence }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-center text-sm text-gray-500">{{ lot.id }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-500">{{ fare_period.name }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-500">${{ total }}</td>
                  <td class="whitespace-nowrap px-2 py-2 text-sm text-gray-500 text-center">
                    <!-- <span :class="colorStatus(status)" class=" rounded-full text-white px-3 py-1 text-xs uppercase font-medium">{{ status }}</span> -->
                    <Menu as="div" class="relative inline-block text-left">
                      <div>
                        <MenuButton 
                        v-if="status.toLowerCase() === 'anulada' && lot.status === 're' "
                        :class="'bg-yellow-500 hover:bg-yellow-400'" class="inline-flex w-32 justify-center rounded-md border border-gray-300  px-4 py-2 text-sm font-bold text-gray-100 shadow-sm  focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100">
                          {{ status }}
                          <!-- <span class="absolute top-0 right-0 px-5 py-1 text-xs tracking-wider text-center uppercase whitespace-no-wrap origin-bottom-left transform rotate-45 -translate-y-full translate-x-1/3 dark:bg-violet-400">Check</span> -->
                        </MenuButton>
                        <MenuButton 
                        v-else
                        :class="colorStatus(status)" class="inline-flex w-32 justify-center rounded-md border border-gray-300  px-4 py-2 text-sm font-bold text-gray-100 shadow-sm  focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100">
                          {{ status }}
                        </MenuButton>
                      </div>

                      <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                        <MenuItems  class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md font-bold bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                          <div class="py-1" v-if="status.toLowerCase() === 'iniciada' || status.toLowerCase() === 'anulada' && lot.status === 're'">
                            
                            <template v-if="status.toLowerCase() === 'iniciada'">
                              <MenuItem v-slot="{ active }">
                              <button  
                              @click="changeStatus(id, lot.id, fare_period.id, client.id, check_in, check_out, licence, 'an')"
                              :class="[active ? 'bg-red-400 text-gray-100' : 'text-red-400 ', 'block w-full px-4 text-left  py-2 text-sm']">Anular</button>
                            </MenuItem>
                            <MenuItem v-slot="{ active }">
                              <button 
                              @click="changeStatus(id, lot.id, fare_period.id, client.id, check_in, check_out, licence, 'fi')"
                              :class="[active ? 'bg-blue-400 text-gray-100' : 'text-blue-400', 'block w-full px-4 text-left  py-2 text-sm']">Finalizar</button>
                            </MenuItem>
                            </template>
                       

                            <template v-if="status.toLowerCase() === 'anulada' && lot.status === 're'">
                            <MenuItem v-slot="{ active }">
                              <button  
                              @click="freeLot(lot.id, 'av')"
                              :class="[active ? 'bg-red-400 text-gray-100' : 'text-red-400 ', 'block w-full px-4 text-left  py-2 text-sm']">Liberar</button>
                            </MenuItem>
                            </template>

                          </div>
                        </MenuItems>
                      </transition>
                    </Menu>
                  </td>
                  <td class="relative whitespace-nowrap py-2 px-2 text-center text-sm font-medium space-x-2">
                    <button
                      @click="isOpenDetail = true, dataReservePeriodDetail = { first_name: client.first_name, last_name: client.last_name, document_number: client.document_number, social_reason: client.social_reason, adress: client.adress, phone: client.phone, email: client.email }"
                      class="text-indigo-600 hover:text-indigo-900 hover:scale-110">
                      <span
                        class="inline-flex items-center justify-center rounded-full bg-blue-100 px-2.5 py-0.5 text-blue-700">
                        <ListDetailsIcon class="-ml-1 mr-1.5 h-4 w-4" />
                        <p class="whitespace-nowrap text-sm">Detalle</p>
                      </span>
                    </button>
                    <button
                      v-if="status.toLowerCase()==='iniciada'"
                      @click="isOpen = true, action = 'update', dataReservePeriod = { id: id, client: client.id, lot: lot, fare_period: fare_period.id, licence: licence, check_in: check_in, check_out: check_out, total: total }"
                      class="text-indigo-600 hover:text-indigo-900 hover:scale-110">
                      <span
                        class="inline-flex items-center justify-center rounded-full bg-amber-100 px-2.5 py-0.5 text-amber-700">
                        <EditCircleIcon class="-ml-1 mr-1.5 h-4 w-4" />
                        <p class="whitespace-nowrap text-sm">Editar</p>
                      </span>
                    </button>
                    <button
                      v-else
                      class="text-indigo-600 hover:text-indigo-900">
                      <span
                        class="inline-flex items-center justify-center rounded-full bg-gray-100 px-2.5 py-0.5 text-gray-700">
                        <EditCircleIcon class="-ml-1 mr-1.5 h-4 w-4" />
                        <p class="whitespace-nowrap text-sm">Editar</p>
                      </span>
                    </button>

                    <!-- <button @click="isOpenDelete = true, dataReservePeriod = { id: id }"
                      class="text-indigo-600 hover:text-indigo-900 hover:scale-110">
                      <span
                        class="inline-flex items-center justify-center rounded-full bg-red-100 px-2.5 py-0.5 text-red-700">
                        <TrashIcon class="-ml-1 mr-1.5 h-4 w-4" />
                        <p class="whitespace-nowrap text-sm">Eliminar</p>
                      </span>
                    </button> -->
                  </td>
                </tr>
                <tr>

                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
	<ol class="flex justify-center gap-1 text-xs font-medium">
		<li>
			<button v-if="showPreviousButton" @click="loadPrevious"
				class="inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100">
				<span class="sr-only">Prev Page</span>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
					<path fill-rule="evenodd"
						d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
						clip-rule="evenodd" />
				</svg>
			</button>
		</li>

		<li>
			<a href="#" class="block h-8 w-8 rounded border border-gray-100 text-center leading-8">
				1
			</a>
		</li>

		<li class="block h-8 w-8 rounded border-blue-600 bg-blue-600 text-center leading-8 text-white">
			2
		</li>

		<li>
			<a href="#" class="block h-8 w-8 rounded border border-gray-100 text-center leading-8">
				3
			</a>
		</li>

		<li>
			<a href="#" class="block h-8 w-8 rounded border border-gray-100 text-center leading-8">
				4
			</a>
		</li>

		<li>
			<button v-if="showNextButton" @click="loadNext"
				class="inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100">
				<span class="sr-only">Next Page</span>
				<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" viewBox="0 0 20 20" fill="currentColor">
					<path fill-rule="evenodd"
						d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
						clip-rule="evenodd" />
				</svg>
			</button>
		</li>
	</ol>
  {{q}}
  <Modal :isOpen="isOpen" :reservePeriod="dataReservePeriod" @toggle="(value) => isOpen = value" :action="action" @loadReservePeriod="() => loadReservePeriod()" />
  <ModalDelete :isOpen="isOpenDelete" :reservePeriod="dataReservePeriod" @toggle="(value) => isOpenDelete = value" @loadReservePeriod="() => loadReservePeriod()" />
  <ModalDetail :isOpen="isOpenDetail" @toggle="(value) => isOpenDetail=value" :reservePeriodDetail="dataReservePeriodDetail" />
</template>
  
<script setup>
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
import { ref } from "vue";
import { TrashIcon, EditCircleIcon, ListDetailsIcon, ChecksIcon } from 'vue-tabler-icons';
import ReservePeriodAPI from "@/services/ReservePeriodAPI"
import LotAPI from "@/services/LotAPI"
import moment from 'moment/min/moment-with-locales';
import Modal from '../components/reserves_period/Modal.vue';
import ModalDelete from '../components/reserves_period/ModalDelete.vue';
import ModalDetail from '../components/reserves_period/ModalDetail.vue';


moment.locale('es'); // default the locale to Spanish

// PAGINATOR
const currentPage = ref(1)
const showNextButton = ref(false)
const showPreviousButton = ref(false)

const loadNext = () => {
	currentPage.value += 1
	loadReservePeriod();
}

const loadPrevious = () => {
	currentPage.value -= 1
	loadReservePeriod();
}


// Cargar todas los pagos
const reservePeriod = ref('')

const q = ref('')

const loadReservePeriod = async () => {
  try {
    // const response = await axios.get('http://127.0.0.1:8000/api/lots/')
    console.log(q.value);
    console.log(currentPage.value);
    const response = await ReservePeriodAPI.getReservePeriodPaginator(currentPage.value, q.value);
    showNextButton.value = false
		showPreviousButton.value = false

    // if (!response.data.results) {
    //     currentPage.value = 1
    // }

		if (response.data.next) {
			showNextButton.value = true
		}

		if (response.data.previous) {
			showPreviousButton.value = true
		}
    
    console.log('cantidad registros:' + response.data.results);
    console.log('cantidad registros:' + response.data.count);
    console.log('siguiente:' + showNextButton.value);
    console.log('anterior:' + showPreviousButton.value);

    console.log(response.data);
    reservePeriod.value = response.data.results;

    // console.log(q.value);
  } catch (error) {

    console.log(error);
  }

}

loadReservePeriod();

// data enviada a modal create and update
const isOpen = ref(false)

const action = ref('')

// data enviada a modal delete
const isOpenDelete = ref(false)

const dataReservePeriod = {}

// data enviada a modal detail
const isOpenDetail = ref(false)
const dataReservePeriodDetail = {}


// Color de estados
const colorStatus = (status_color) => {
    if (status_color.toLowerCase() === 'iniciada') return 'bg-green-500 hover:bg-green-400'
    if( status_color.toLowerCase() === 'anulada' ) return 'bg-red-500 hover:bg-red-400'
    if( status_color.toLowerCase() === 'finalizada' ) return 'bg-blue-500 hover:bg-blue-400'
    if( status_color.toLowerCase() === 'reservada' ) return 'bg-orange-500 hover:bg-orange-400'
}

// Liberar Estacionamiento
const freeLot = (id, status) => {
  LotAPI.updateLot(id, {'status': status})
  .then(res => {
        console.log(res)
        loadReservePeriod();
      })
  .catch(error => {
    if (error.response) {
      for (const property in error.response.data) {
        errors.value.push(`${property}: ${error.response.data[property]}`);
        // property === 'lot' && setOpen(false)
        // property === 'lot' &&  (errors.value = [])
      };

      console.log(JSON.stringify(error.response.data));
    }
    else if (error.message) {
      errors.value.push('Algo salio mal, porfavor intenta nuevamente')
      console.log(JSON.stringify(error));
    }
  })
}

// errores
const errors = ref([])

const formDataChangeStatus = ref({
  lot: '',
  fare_period: '',
  client: null,
  licence: '',
  status: '',
  check_in: '',
  check_out: '',
  total: '',
})

// Cambiar estado
const changeStatus = (id, lot, fare_period, client, check_in, check_out, licence, status) => {
  formDataChangeStatus.value = {lot, fare_period, client, check_in, check_out, licence, status}
  console.log(formDataChangeStatus.value);
  ReservePeriodAPI.updateReservePeriod(id, formDataChangeStatus.value)
  .then(res => {
        console.log(res)
        loadReservePeriod();
      })
  .catch(error => {
    if (error.response) {
      for (const property in error.response.data) {
        errors.value.push(`${property}: ${error.response.data[property]}`);
        // property === 'lot' && setOpen(false)
        // property === 'lot' &&  (errors.value = [])
      };

      console.log(JSON.stringify(error.response.data));
      loadReservePeriod();
    }
    else if (error.message) {
      errors.value.push('Algo salio mal, porfavor intenta nuevamente')
      console.log(JSON.stringify(error));
    }
  })
}

</script>