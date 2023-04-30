<script lang="ts">
import Product from "./components/Product.vue"
export default {
    components: {
        Product
    },
    data() {
        return {
            items: [
                {
                    "id": 1,
                    "name": "Product A",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 9.99,
                    "image_url": "https://example.com/product-a.jpg"
                },
                {
                    "id": 2,
                    "name": "Product B",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 14.99,
                    "image_url": "https://example.com/product-b.jpg"
                },
                {
                    "id": 3,
                    "name": "Product C",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 24.99,
                    "image_url": "https://example.com/product-c.jpg"
                },
                {
                    "id": 4,
                    "name": "Product D",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 19.99,
                    "image_url": "https://example.com/product-d.jpg"
                },
                {
                    "id": 5,
                    "name": "Product E",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 12.99,
                    "image_url": "https://example.com/product-e.jpg"
                },
                {
                    "id": 6,
                    "name": "Product F",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "price": 29.99,
                    "image_url": "https://example.com/product-f.jpg"
                }
            ]
        }
    }
}
</script>

<template>
    <div class="px-4 py-6">
        <h2 class="text-xl font-semibold mb-4">Browse Materials</h2>

        <div class="grid grid-cols-4 gap-4">
            <Product v-for="item in items" :item="item"></Product>
        </div>
    </div>
</template>

<style></style>