<script setup>
import { onBeforeMount } from 'vue';
import { useAuthStore } from "@/stores/auth.js";
import axios from 'axios';;
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

<template class="h-full bg-gray-100">

    <SideBar />
</template>

<style >

</style>
