<template>
    <TransitionRoot appear :show="isOpen" as="template">
        <Dialog as="div" @close="setOpen(false)" class="relative z-10" >
            <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100"
                leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-black bg-opacity-25" />
            </TransitionChild>

            <div class="fixed inset-0 overflow-y-auto">
                <div class="flex min-h-full items-center justify-center p-4 text-center">
                    <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95"
                        enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100"
                        leave-to="opacity-0 scale-95">
                        <DialogPanel class="inline-block p-4 overflow-hidden align-bottom transition-all transform dark:bg-gray-800 bg-white rounded-lg shadow-2xl lg:p-8  sm:align-middle sm:max-w-sm sm:w-full">
                            <!-- <DialogTitle></DialogTitle> -->
                            <div>
                                <div class="mt-3  sm:mt-5">
                                    <h1
                                        class="mb-8 text-2xl font-extrabold leading-none tracking-tighter dark:text-white text-neutral-600">
                                        Información Adicional
                                    </h1>
                                </div>
                            </div>
                            <ul class="">
                                <li class="flex text-base text-body-color mb-4">
                                    <span class="
                                        rounded-full
                                        mr-2
                                        text-base text-primary
                                        flex
                                        items-center
                                        ">
                                        <svg width="20" height="8" viewBox="0 0 20 8" class="fill-current">
                                            <path d="M19.2188 2.90626L17.0625 0.343758C16.875 0.125008 16.5312 0.0937583 16.2812 0.281258C16.0625 0.468758 16.0312 0.812508 16.2188 1.06251L18.25 3.46876H0.9375C0.625 3.46876 0.375 3.71876 0.375 4.03126C0.375 4.34376 0.625 4.59376 0.9375 4.59376H18.25L16.2188 7.00001C16.0312 7.21876 16.0625 7.56251 16.2812 7.78126C16.375 7.87501 16.5 7.90626 16.625 7.90626C16.7812 7.90626 16.9375 7.84376 17.0312 7.71876L19.1875 5.15626C19.75 4.46876 19.75 3.53126 19.2188 2.90626Z"></path>
                                        </svg>
                                    </span>
                                    <b class="mr-2">Patente: </b> {{ props.reserve.licence }}
                                </li>
                                <li class="flex text-base text-body-color mb-4">
                                    <span class="
                                        rounded-full
                                        mr-2
                                        text-base text-primary
                                        flex
                                        items-center
                                        ">
                                        <svg width="20" height="8" viewBox="0 0 20 8" class="fill-current">
                                            <path d="M19.2188 2.90626L17.0625 0.343758C16.875 0.125008 16.5312 0.0937583 16.2812 0.281258C16.0625 0.468758 16.0312 0.812508 16.2188 1.06251L18.25 3.46876H0.9375C0.625 3.46876 0.375 3.71876 0.375 4.03126C0.375 4.34376 0.625 4.59376 0.9375 4.59376H18.25L16.2188 7.00001C16.0312 7.21876 16.0625 7.56251 16.2812 7.78126C16.375 7.87501 16.5 7.90626 16.625 7.90626C16.7812 7.90626 16.9375 7.84376 17.0312 7.71876L19.1875 5.15626C19.75 4.46876 19.75 3.53126 19.2188 2.90626Z"></path>
                                        </svg>
                                    </span>
                                    <b class="mr-2">Numero Estacionamiento: </b> {{ props.reserve.lot.name }}
                                </li>
                                <li class="flex text-base text-body-color mb-4">
                                    <span class="
                                        rounded-full
                                        mr-2
                                        text-base text-primary
                                        flex
                                        items-center
                                        ">
                                        <svg width="20" height="8" viewBox="0 0 20 8" class="fill-current">
                                            <path d="M19.2188 2.90626L17.0625 0.343758C16.875 0.125008 16.5312 0.0937583 16.2812 0.281258C16.0625 0.468758 16.0312 0.812508 16.2188 1.06251L18.25 3.46876H0.9375C0.625 3.46876 0.375 3.71876 0.375 4.03126C0.375 4.34376 0.625 4.59376 0.9375 4.59376H18.25L16.2188 7.00001C16.0312 7.21876 16.0625 7.56251 16.2812 7.78126C16.375 7.87501 16.5 7.90626 16.625 7.90626C16.7812 7.90626 16.9375 7.84376 17.0312 7.71876L19.1875 5.15626C19.75 4.46876 19.75 3.53126 19.2188 2.90626Z"></path>
                                        </svg>
                                    </span>
                                    <b class="mr-2">Tipo Estacionamiento: </b> {{ props.reserve.type }}
                                </li>
                                <li class="flex text-base text-body-color mb-4">
                                    <span class="
                                        rounded-full
                                        mr-2
                                        text-base text-primary
                                        flex
                                        items-center
                                        ">
                                        <svg width="20" height="8" viewBox="0 0 20 8" class="fill-current">
                                            <path d="M19.2188 2.90626L17.0625 0.343758C16.875 0.125008 16.5312 0.0937583 16.2812 0.281258C16.0625 0.468758 16.0312 0.812508 16.2188 1.06251L18.25 3.46876H0.9375C0.625 3.46876 0.375 3.71876 0.375 4.03126C0.375 4.34376 0.625 4.59376 0.9375 4.59376H18.25L16.2188 7.00001C16.0312 7.21876 16.0625 7.56251 16.2812 7.78126C16.375 7.87501 16.5 7.90626 16.625 7.90626C16.7812 7.90626 16.9375 7.84376 17.0312 7.71876L19.1875 5.15626C19.75 4.46876 19.75 3.53126 19.2188 2.90626Z"></path>
                                        </svg>
                                    </span>
                                    <b class="mr-2">Tarifa: </b> ${{ props.reserve.fare.price }}
                                </li>
                            </ul>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
</template>
  
<script setup>
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
} from '@headlessui/vue'


// pasar valor del padre al hijo - en este caso abrir modal
const props = defineProps({
  isOpen: Boolean,
  reserve: Object
})

// console.log(props.reserve);

// pasar valor del hijo al padre - en este caso cerrar el modal
const emit = defineEmits(['toggle']);

const setOpen = (value) => {
    // usamos el emit porque el padre debe hacer el cambio de estado
    emit('toggle', value);
}

</script>
