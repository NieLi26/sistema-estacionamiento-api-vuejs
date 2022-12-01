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
                            <!-- TITLE -->
                            <div class="items-center flex justify-between">
                                <div class="flex items-center">
                                    <span
                                        class="inline-flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-green-200 text-white">
                                        <PlusIcon class="h-6 w-6" aria-hidden="true" />
                                    </span>
                                    <p class="text-xl font-bold ml-2 sm:mt-0 sm:ml-3">
                                        {{ props.action === 'create' ? 'Creación de Cliente' : 'Actualización de Cliente'}}
                                    </p>
                                </div>

                                <button type="button"
                                    class="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                    @click="setOpen(false)">
                                    <span class="sr-only">Close</span>
                                    <XIcon class="h-6 w-6" aria-hidden="true" />
                                </button>
                            </div>

                            <!-- INPUTS -->
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="first_name"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.first_name" type="text" id="first_name"
                                            placeholder="Nombre"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Nombre
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="last_name"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.last_name" type="text" id="last_name"
                                            placeholder="Apellido"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Apellido
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="document_number"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.document_number" type="text" id="document_number"
                                            placeholder="Número Documento"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Número Documento
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="social_reason"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.social_reason" type="text" id="social_reason"
                                            placeholder="Razón Social"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Razón Social
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="adress"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.adress" type="text" id="adress" placeholder="Dirección"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Dirección
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="phone"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.phone" type="text" id="phone" placeholder="ej. +999999999"
                                            maxlength="9"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Teléfono
                                        </span>
                                    </label>
                                </div>
                            </div>
                            <div class="my-6 text-center sm:my-8">
                                <div class="mt-2">
                                    <label for="email"
                                        class="relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
                                        <input v-model="formData.email" type="text" id="email"
                                            placeholder="Correo Electrónico"
                                            class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm" />

                                        <span
                                            class="absolute left-3 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs">
                                            Correo Electrónico
                                        </span>
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="mt-5 sm:mt-6 sm:grid sm:grid-cols-2 sm:gap-3 sm:grid-flow-row-dense">
                            <button type="button"
                                class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:col-start-2 sm:text-sm"
                                @click="handleSubmit">
                                Guardar
                            </button>
                            <button type="button"
                                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:col-start-1 sm:text-sm"
                                @click="setOpen(false)" ref="cancelButtonRef">
                                Cancel
                            </button>
                        </div>

                        <!-- Alert -->
                        <div v-if="errors.length"
                            class="mt-5 sm:mt-6 bg-yellow-200 border-yellow-600 text-yellow-600 border-l-4 p-4"
                            role="alert">
                            <p class="font-bold">
                                Error
                            </p>
                            <p v-for="error in errors" :key="error">
                                {{ error }}
                            </p>
                        </div>
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
import ClientAPI from '../../services/ClientAPI';


watch(() => props.isOpen, () => {

    errors.value = []

    if (props.action === 'update') {
        formData.first_name = props.client.first_name
        formData.last_name = props.client.last_name
        formData.document_number = props.client.document_number
        formData.social_reason = props.client.social_reason
        formData.adress = props.client.adress
        formData.phone = props.client.phone
        formData.email = props.client.email
    }

    if (!props.isOpen) {
        formData.first_name = ''
        formData.last_name = ''
        formData.document_number = ''
        formData.social_reason = ''
        formData.adress = ''
        formData.phone = ''
        formData.email = ''
    }


})

// pasar valor del padre al hijo - en este caso abrir modal
const props = defineProps({
    isOpen: Boolean,
    client: Object,
    action: String
})

// console.log(props.reserve);

// pasar valor del hijo al padre - en este caso cerrar el modal
const emit = defineEmits(['toggle', 'loadClients']);

const setOpen = (value) => {
    // usamos el emit porque el padre debe hacer el cambio de estado, debemos avisarle del cambio, en este caso a false
    emit('toggle', value);
}


const formData = {
    first_name: '',
    last_name: '',
    document_number: '',
    social_reason: '',
    adress: '',
    phone: '',
    email: ''
}


const errors = ref([])

const handleSubmit = () => {
    errors.value = []
    console.log(formData);
    formData.first_name === '' && errors.value.push('No ingreso nombre')
    formData.last_name === '' && errors.value.push('No ingreso apellido')
    formData.document_number === '' && errors.value.push('No ingreso número de documento')
    formData.adress === '' && errors.value.push('No ingreso dirección')
    formData.phone === '' && errors.value.push('No ingreso teléfono')
    formData.email === '' && errors.value.push('No ingreso correo eléctronico')

    let numericTest = /^[0-9-]+$/;
    !numericTest.test(formData.document_number) && formData.document_number !== '' && errors.value.push('Numero de documento: Solo deben contener numeros')
    !numericTest.test(formData.phone) && formData.phone !== '' && errors.value.push('Teléfono: Solo deben contener numeros')

    if (!errors.value.length) {
        let requestMethod = ''

        props.action === 'create' ? requestMethod = ClientAPI.createClient(formData) : requestMethod = ClientAPI.updateClient(props.client.id, formData) 

        requestMethod
            .then(res => {
                console.log(res)
                emit('loadClients');
                setOpen(false);
            })
            .catch(error => {
                if (error.response) {
                    for (const client in error.response.data) {
                        errors.value.push(`${client}: ${error.response.data[client]}`);
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


</script>