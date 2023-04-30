<script lang="ts">
export default {
    props: [
        'item'
    ]
}
</script>

<template>
    <div class="bg-gray-100 rounded-lg p-4">
        <div class="mb-4">
            <img src="https://placehold.co/300x200" alt="Product 1 thumbnail" class="w-full rounded-lg">
        </div>
        <div>
            <h2 class="text-lg font-semibold mb-2">Product Name</h2>
            <p class="text-gray-700">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam euismod commodo
                augue vitae blandit. Sed euismod est sed lectus posuere porta.</p>
        </div>
    </div>
</template>

<style>

</style>