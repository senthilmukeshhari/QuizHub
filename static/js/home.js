
var images = document.querySelectorAll('.background-images img');
var currentIndex = 0;

window.addEventListener('load', () => {
    setTimeout(() => {
        let login_box = document.querySelector('.login-box')

        login_box.classList.add('animate')
    }, 2800);
})


function changeImage() {
    images[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add('active');
}

setInterval(changeImage, 3000);

let input = document.querySelector('#user_name')
let form = document.querySelector('form')
let error_msg = document.querySelector('.invaild-feedback')

form.addEventListener('submit', (e) => {
    if (input.value == '') {
        error_msg.innerText = 'Please enter your name'
        e.preventDefault()
    }
})