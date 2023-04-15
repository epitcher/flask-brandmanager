<script lang="ts">
export default {
    name: "App",
    data() {
        return { count: 0 };
    },
}
</script>

<template>
    <div>
        <button @click="count++">increment</button>
        <button @click="count--">decrement</button>
        <p>{{ count }}</p>
    </div>
</template>
