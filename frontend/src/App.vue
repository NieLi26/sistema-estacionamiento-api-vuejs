<script setup>
import { RouterView } from 'vue-router'
import NavBar from "./components/navigation/NavBar.vue";
import Footer from "./components/navigation/Footer.vue";
import { onBeforeMount } from 'vue';
import { useAuthStore } from "@/stores/auth.js";
import axios from 'axios';
import LeftSideBar from './components/navigation/LeftSideBar.vue';
import SideBar from './components/navigation/SideBar.vue';

const store = useAuthStore();

onBeforeMount(() => {
    store.initializeStore();

    const token = store.user.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
});

</script>

<template>
    <!-- <div class="h-screen flex overflow-hidden bg-gray-100">
        <LeftSideBar />
        <div class="flex flex-col w-0 flex-1 overflow-hidden ">
            <NavBar />
            <main class="flex-1 relative overflow-y-auto overflow-x-hidden focus:outline-none">
       
                    <RouterView />
                    <Footer />
        
            </main>
    
        </div>
    </div> -->
    <SideBar />
</template>

<style >

</style>
