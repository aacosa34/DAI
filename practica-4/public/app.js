const dark_mode = document.querySelector('#dark-mode')
const root = document.documentElement

dark_mode.addEventListener('click', () => {
    if(!root.classList.contains('dark')) {
        root.classList.add('dark')
    } else {
        root.classList.remove('dark')
    }
})