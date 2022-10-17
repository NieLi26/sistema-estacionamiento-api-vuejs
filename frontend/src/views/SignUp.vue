<template>

    <div class="flex flex-wrap w-full">
        <div class="flex flex-col w-full md:w-1/2">
            <div class="flex justify-center pt-12 md:justify-start md:pl-12 md:-mb-24">
                <a href="#" class="p-4 text-xl font-bold text-white bg-black">
                    Design.
                </a>
            </div>
            <div class="flex flex-col justify-center px-8 pt-8 my-auto md:justify-start md:pt-0 md:px-24 lg:px-32">
                <p class="text-3xl text-center">
                    Register.
                </p>
                <form @submit.prevent="handleSubmit" class="flex flex-col pt-3 md:pt-8">
                    <div class="flex flex-col pt-4">
                        <div class="flex relative ">
                            <span
                                class=" inline-flex  items-center px-3 border-t bg-white border-l border-b  border-gray-300 text-gray-500 shadow-sm text-sm">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                                    width="15" height="15">
                                    <path fill-rule="evenodd"
                                        d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z"
                                        clip-rule="evenodd" />
                                </svg>
                            </span>
                            <input type="text" v-model="formData.username"
                                class=" flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                placeholder="Username" />
                        </div>
                    </div>
                    <div class="flex flex-col pt-4 mb-12 space-y-4">
                        <div class="flex relative ">
                            <span
                                class=" inline-flex  items-center px-3 border-t bg-white border-l border-b  border-gray-300 text-gray-500 shadow-sm text-sm">
                                <svg width="15" height="15" fill="currentColor" viewBox="0 0 1792 1792"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M1376 768q40 0 68 28t28 68v576q0 40-28 68t-68 28h-960q-40 0-68-28t-28-68v-576q0-40 28-68t68-28h32v-320q0-185 131.5-316.5t316.5-131.5 316.5 131.5 131.5 316.5q0 26-19 45t-45 19h-64q-26 0-45-19t-19-45q0-106-75-181t-181-75-181 75-75 181v320h736z">
                                    </path>
                                </svg>
                            </span>
                            <input type="password" v-model="formData.password"
                                class=" flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                placeholder="Password" />
                        </div>
                        <div class="flex relative ">
                            <span
                                class=" inline-flex  items-center px-3 border-t bg-white border-l border-b  border-gray-300 text-gray-500 shadow-sm text-sm">
                                <svg width="15" height="15" fill="currentColor" viewBox="0 0 1792 1792"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M1376 768q40 0 68 28t28 68v576q0 40-28 68t-68 28h-960q-40 0-68-28t-28-68v-576q0-40 28-68t68-28h32v-320q0-185 131.5-316.5t316.5-131.5 316.5 131.5 131.5 316.5q0 26-19 45t-45 19h-64q-26 0-45-19t-19-45q0-106-75-181t-181-75-181 75-75 181v320h736z">
                                    </path>
                                </svg>
                            </span>
                            <input type="password" v-model="formData.password2"
                                class=" flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                placeholder="Password2" />
                        </div>
                    </div>
                    <button type="submit"
                        class="w-full px-4 py-2 text-base font-semibold text-center text-white transition duration-200 ease-in bg-black shadow-md hover:text-black hover:bg-white focus:outline-none focus:ring-2">
                        <span class="w-full">
                            Submit
                        </span>
                    </button>
                </form>

                <div v-if="errors.length" role="alert" class="mt-2">
                    <div class="flex items-center justify-between bg-red-500 text-white font-bold rounded-t px-4 py-2">
                        <div>Danger</div>
                        <button @click="closeAlert">x</button>
                    </div>
                    <div class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                        <p v-for="error in errors" :key="error">
                            {{ error }}
                        </p>
                    </div>
                </div>
          
                <div class="pt-12 pb-12 text-center">
                    <p>
                        Do you have an account?
                        <RouterLink class="font-semibold underline" to="/signin">Click here </RouterLink>
                        to Sing in
                    </p>
                </div>
            </div>
        </div>
        <div class="w-1/2 shadow-2xl">
            <img class="hidden object-cover w-full h-screen md:block"
                src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngarts.com%2Ffiles%2F6%2FCar-Parking-Download-PNG-Image.png&f=1&nofb=1" />
        </div>
    </div>

</template>
    
<script setup>
import { ref } from 'vue';
import AuthAPI from "@/services/AuthAPI";
import router from '../router';

const closeAlert = () => {
        errors.value = []
    }

const formData = {
    username: '',
    password: '',
    password2: '',
}

const errors = ref([])


const handleSubmit = () => {
    errors.value = []

    formData.username === '' && errors.value.push('El campo username no puede estar vacio')
    formData.password === '' && errors.value.push('El campo password no puede estar vacio')
    formData.password2 === '' && errors.value.push('El campo password2 no puede estar vacio')
    formData.password2 !== formData.password && errors.value.push('Las contraseñas deben coincidir')

    console.log(errors);

    if (!errors.value.length) {
        AuthAPI.createUser(formData)
            .then(res => {
                console.log(res)
                router.push("/signin");
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
}


</script>