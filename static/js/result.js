window.addEventListener('load', () => {

    setTimeout(() => {
        if (score == 4 || score == 5) {
            confetti.start()
            setTimeout(() => {
                confetti.stop()
            }, 5000);
        }
    }, 2800)

    const result_percentage = document.querySelector('.result-percentage').children[0]
    const result_img = document.querySelector('.result-img')
    const circle = document.querySelectorAll('circle')[0]
    const greetingsEl = document.querySelector('.greetings')
    if (score == 5) {
        circle.style.strokeDashoffset = Math.floor(630 - ((630 / 100) * 100))
        circle.style.stroke = "#198754"
        result_percentage.innerText = '100'
        result_img.src = five_img
        greetingsEl.innerText = "Congratulations"
    }
    if (score == 4) {
        circle.style.strokeDashoffset = Math.floor(630 - ((630 / 100) * 80))
        circle.style.stroke = "#198754"
        result_percentage.innerText = '80'
        result_img.src = four_img
        greetingsEl.innerText = "Well Done"
    }
    if (score == 3) {
        circle.style.strokeDashoffset = Math.floor(630 - ((630 / 100) * 60))
        circle.style.stroke = "#ffc107"
        result_percentage.innerText = '60'
        result_img.src = three_and_two_img
        greetingsEl.innerText = "Nice Try"
    }
    if (score == 2) {
        circle.style.strokeDashoffset = Math.floor(630 - ((630 / 100) * 40))
        circle.style.stroke = "#ffc107"
        result_percentage.innerText = '40'
        result_img.src = three_and_two_img
        greetingsEl.innerText = "Better Luck Next Time"
    }
    if (score == 1) {
        circle.style.strokeDashoffset = Math.floor(630 - ((630 / 100) * 20))
        circle.style.stroke = "#dc3545"
        result_percentage.innerText = '20'
        result_img.src = one_img
        greetingsEl.innerText = "Good Luck"
    }
})



// Feedd Back

function selectOpt() {
    let input = document.querySelectorAll('input[type=radio]')
    input.forEach(ele => {
        if (ele.checked) {
            ele.nextElementSibling.classList.add('imgstyle')
            ele.parentElement.classList.add('labelstyle')
        } else {
            ele.nextElementSibling.classList.remove('imgstyle')
            ele.parentElement.classList.remove('labelstyle')
        }
    });
}

let formEl = document.forms.feedback_form
let errEl = document.querySelector('.err')

formEl.addEventListener('submit', (e) => {
    e.preventDefault()
    let input = formEl.feedback;
    if (input.value == '') {
        errEl.innerText = "Please Chioce any one option."
    } else {
        errEl.innerText = ""
        $('#Mymodal').modal('show')
        setTimeout(() => {
            $('form').submit()
        },1000)
    }
})