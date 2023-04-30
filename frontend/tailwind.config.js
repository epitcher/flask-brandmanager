module.exports = {
    mode: 'jit',
    purge: [
        './../app/modules/user/views/**/*.html',
        './../app/modules/admin/views/**/*.html',
        './src/*.vue',
        './src/**/.vue'
    ],
    theme: {
        extend: {}
    },
    variants: {},
    plugins: []
}
