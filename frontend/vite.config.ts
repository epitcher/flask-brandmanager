import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: '../app/static/dist', // Replace with your desired directory name
    assetsDir: 'static', // Optional: customize the assets directory (default is '_assets')
    rollupOptions: {
      output: {
        entryFileNames: 'js/[name].[hash].js', // Customize your JavaScript output file name
        chunkFileNames: 'js/[name].[hash].js', // Customize your JavaScript chunk file name
        assetFileNames: 'css/[name].[hash].css', // Customize your CSS output file name
      },
    },
  },
})
