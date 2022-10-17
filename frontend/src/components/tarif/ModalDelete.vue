<template>
    <TransitionRoot appear :show="isOpen" as="template">
        <Dialog as="div" @close="setOpen(false)" class="relative z-10">
            <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100"
                leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-black bg-opacity-25" />
            </TransitionChild>

            <div class="fixed inset-0 overflow-y-auto">
                <div class="flex min-h-full items-center justify-center p-4 text-center">
                    <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95"
                        enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100"
                        leave-to="opacity-0 scale-95">
                        <DialogPanel
                            class="flex flex-col max-w-md gap-2 p-6 rounded-md shadow-md bg-white dark:bg-gray-900 dark:text-gray-100">
                            <h2 class="flex items-center gap-2 text-xl font-semibold leading-tight tracking-wide">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-6 h-6 fill-current shrink-0 dark:text-violet-400">
                                    <path d="M451.671,348.569,408,267.945V184c0-83.813-68.187-152-152-152S104,100.187,104,184v83.945L60.329,348.568A24,24,0,0,0,81.432,384h86.944c-.241,2.636-.376,5.3-.376,8a88,88,0,0,0,176,0c0-2.7-.135-5.364-.376-8h86.944a24,24,0,0,0,21.1-35.431ZM312,392a56,56,0,1,1-111.418-8H311.418A55.85,55.85,0,0,1,312,392ZM94.863,352,136,276.055V184a120,120,0,0,1,240,0v92.055L417.137,352Z"></path>
                                    <rect width="32" height="136" x="240" y="112"></rect>
                                    <rect width="32" height="32" x="240" y="280"></rect>
                                </svg>Estas seguro de eliminar este registro?
                            </h2>
                            <p class="flex-1 dark:text-gray-400">Si eliminas este registro no podras recuperarlo.</p>
                            <div class="flex flex-col justify-center gap-3 mt-6 sm:flex-row">
                                <button @click="setOpen(false)" class="px-6 py-2 rounded-sm border border-gray-300 shadow-sm">Cancelar</button>
                                <button @click="handleDelete" class="px-6 py-2 rounded-sm shadow-sm bg-red-300 text-gray-900 dark:text-white">Confirmar</button>
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
import { ref } from 'vue'
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
} from '@headlessui/vue'
import FareAPI from '../../services/FareAPI';

// pasar valor del padre al hijo - en este caso abrir modal
const props = defineProps({
  isOpen: Boolean,
  fare: Object,
//   action: String
})

// pasar valor del hijo al padre - en este caso cerrar el modal
const emit = defineEmits(['toggle', 'loadFares']);

const setOpen = (value) => {
    // usamos el emit porque el padre debe hacer el cambio de estado, debemos avisarle del cambio, en este caso a false
    emit('toggle', value);
}

const errors = ref([])

const handleDelete = () => {
    errors.value = []

    FareAPI.deleteFare(props.fare.id)
      .then(res => {
        console.log(res)
        emit('loadFares');
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

</script>
  