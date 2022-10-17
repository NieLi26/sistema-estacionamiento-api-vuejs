<template>
    <label>{{ label }}</label>
    <input 
    :placeholder="label"
    :value="modelValue"
    :class="class"  
    :type="type"              
    @input="$emit('update:modelValue', $event.target.value)"
    >
    <!-- $event.target.value, es el valor que el v-model recibira del componente padre  -->
    <!-- v-bind="$attrs" , en este caso es para que reciba las clases en css" -->
</template>

<script setup>

    defineProps({
        label: {
            type: String,
            default: ''
        },
        modelValue: {
            type: [String, Number, Date],
            default: ''
        },
        class: {
            type: String,
            default: ''
        },
        type: {
            type: String,
            default: ''
        },
    })

    // defineProps({
    //     label: String,
    //     modelValue: [String, Number]
    // })


</script>