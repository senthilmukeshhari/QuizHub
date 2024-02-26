window.history.forward()

window.addEventListener('load', () => {
    setTimeout(() => {
        let spinner = document.querySelector('.spinner')

        spinner.classList.add('d-none')
    }, 2700);
})
