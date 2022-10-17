<template>
	<div class="container p-2 mx-auto sm:p-4 text-gray-900 dark:text-gray-100">
		<h2 class="mb-4 text-2xl font-semibold leading-tight">Invoices</h2>
		<div class="overflow-x-auto">
			<table class="min-w-full text-xs">
				<colgroup>
					<col>
					<col>
					<col>
					<col>
					<col>
					<col class="w-24">
				</colgroup>
				<thead class="bg-gray-100 dark:bg-gray-700">
					<tr class="text-left">
						<th class="p-3">Id #</th>
						<th class="p-3">Patente</th>
						<th class="p-3">Nro Boleta</th>
						<th class="p-3">Fecha Creación</th>
						<th class="p-3 text-right">Valor</th>
						<th class="p-3">Acciones</th>
					</tr>
				</thead>
				<tbody class="">
					<tr
                    v-for="{id, licence, number, created_at, total} in payments" :key="id" 
                    class="border-b border-opacity-40 dark:border-opacity-20 border-gray-400 dark:border-gray-700 dark:bg-gray-900">
						<td class="p-3">
							<p>{{ id }}</p>
						</td>
						<td class="p-3">
							<p class="uppercase">{{ licence }}</p>
						</td>
						<td class="p-3">
							<p>{{ number }}</p>
						</td>
						<td class="p-3">
							<p>{{ moment(created_at).format('DD MMM YYYY') }}</p>
                            <p class="text-gray-400">{{ moment(created_at).format('dddd') }}</p>
						</td>
						<td class="p-3 text-right">
							<p>${{ total }}</p>
						</td>
						<td class="p-3 text-right">
							<!-- <span class="px-3 py-1 font-semibold rounded-md bg-violet-400 text-gray-900">
								<span>Pending</span>
							</span> -->
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>


<script setup>
import { ref } from "vue";
import PaymentAPI from "@/services/PaymentAPI"
import moment from 'moment/min/moment-with-locales';

moment.locale('es'); // default the locale to Spanish

// Cargar todas los pagos
const payments = ref('')

const loadPayments = async () => {
    try {
        const response = await PaymentAPI.getPayments();
        // setTimeout(() => {
            payments.value = response.data;
            console.log(payments.value);
        // }, 3000)
    } catch (error) {
        console.log(error);
    }
};

loadPayments();


</script>