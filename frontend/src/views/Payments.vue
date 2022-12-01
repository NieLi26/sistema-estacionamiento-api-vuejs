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
						<input @keyup="loadReservePeriod" v-model='q' type="search" name="Search"
							placeholder="Search..."
							class="w-64 py-2 pl-10 text-sm rounded-md sm:w-full focus:outline-none dark:bg-gray-800 dark:text-gray-100 focus:dark:bg-gray-900 focus:dark:border-violet-400">
					</div>
				</fieldset>
			</div>
			<!-- <div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
				<button
					@click="isOpen = true, action = 'create', dataReservePeriod = { check_in: '', check_out: '', fare_period: '', lot: '' }"
					type="button"
					class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto">Agregar</button>
			</div> -->
		</div>
		<div class="mt-8 flex flex-col">
			<div class="-my-2 -mx-4 sm:-mx-6 lg:-mx-8">
				<div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
					<div class="shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
						<table class="min-w-full divide-y divide-gray-300">
							<thead class="bg-gray-50 dark:bg-gray-700">
								<tr class="text-left">
									<th
										class="whitespace-nowrap py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
										ID</th>
									<th
										class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
										Patente</th>
									<th
										class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
										Nro Boleta</th>
									<th
										class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">
										Fecha Creación</th>
									<th
										class="whitespace-nowrap px-2 py-3.5 text-rigth text-sm font-semibold text-gray-900 ">
										Valor</th>
									<!-- <th class="whitespace-nowrap px-2 py-3.5 text-left text-sm font-semibold text-gray-900">Acciones</th> -->
								</tr>
							</thead>
							<tbody class="divide-y divide-gray-200 bg-white ">
								<tr v-for="{ id, licence, number, created_at, total } in payments" :key="id"
									class="border-b border-opacity-40 dark:border-opacity-20 border-gray-400 bg-white dark:border-gray-700 dark:bg-gray-900">
									<td class="whitespace-nowrap py-2 pl-4 pr-3 text-sm text-gray-500 sm:pl-6">
										<p>{{ id }}</p>
									</td>
									<td class="whitespace-nowrap px-2 py-2 text-xs font-medium text-gray-900">
										<p class="uppercase">{{ licence }}</p>
									</td>
									<td class="whitespace-nowrap px-2 py-2 text-xs font-medium text-gray-900">
										<p>{{ number }}</p>
									</td>
									<td class="whitespace-nowrap px-2 py-2 text-xs font-medium text-gray-900">
										<p>{{ moment(created_at).format('DD MMM YYYY') }}</p>
										<p class="text-gray-400">{{ moment(created_at).format('dddd') }}</p>
									</td>
									<td class="whitespace-nowrap px-2 py-2 text-xs font-medium text-gray-900 ">
										<p>${{ total }}</p>
									</td>
									<!-- <td class="whitespace-nowrap px-2 py-2 text-xs font-medium text-gray-900 t">
						<span class="px-3 py-1 font-semibold rounded-md bg-violet-400 text-gray-900">
							<span>Pending</span>
						</span>
					</td> -->
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
</template>

<script setup>
import { ref } from "vue";
import PaymentAPI from "@/services/PaymentAPI"
import moment from 'moment/min/moment-with-locales';

moment.locale('es'); // default the locale to Spanish

// PAGINATOR
const currentPage = ref(1)
const showNextButton = ref(false)
const showPreviousButton = ref(false)

const loadNext = () => {
	currentPage.value++
	loadPayments();
}

const loadPrevious = () => {
	currentPage.value--
	loadPayments();
}


// Cargar todas los pagos
const payments = ref('')

const loadPayments = async () => {
	try {
		const response = await PaymentAPI.getPaymentsPaginator(currentPage.value);
		// setTimeout(() => {
		showNextButton.value = false
		showPreviousButton.value = false

		if (response.data.next) {
			showNextButton.value = true
		}

		if (response.data.previous) {
			showPreviousButton.value = true
		}

		payments.value = response.data.results;
		console.log(payments.value);
		// }, 3000)
	} catch (error) {
		console.log(error);
	}
};

loadPayments();


</script>