$('form[name=questionsForm]').children().last().find('button').text('Submit').addClass('fw-bold')

//  Animation
window.addEventListener('load', () => {

    setTimeout(() => {
        $("#user-card").addClass('animate')
        let typed = new Typed("#user", {
            strings: [type_user],
            typeSpeed: 90,
            backSpeed: 90,
            showCursor: false
        })
        $('#user').addClass('typing')
    }, 2800);
})

// Showing questions cards
$('#start-btn').click((e) => {

    e.target.disabled = true
    let currentCard = e.target.closest('.card')
    nextCard = currentCard.nextElementSibling.children[1]

    nextCard.classList.remove('d-none')
    scrollTo(0, document.body.scrollHeight)
    nextCard.classList.add('animate')

    // when start btn in clicking, display and start timer
    e.target.disabled = true
    $('.timer').removeClass('d-none')
    let minutes = 9, seconds = 60
    let timer = setInterval(() => {
        seconds--
        if (seconds < 0) {
            minutes--
            seconds = 59
        }
        displayTimer(seconds, minutes)
        if (minutes == 0 && seconds == 0) {
            clearInterval(timer)
            $('.spinner').removeClass('d-none')
            validation()
        }
    }, 100);
})

function displayTimer(ss, mm) {
    if (mm == 0 && ss <= 59) {
        $('.minutes').addClass('text-danger')
        $('.seconds').addClass('text-danger')
    }
    mm = mm <= 9 ? '0' + mm : mm
    ss = ss <= 9 ? '0' + ss : ss
    $('.minutes').text(mm + " : ")
    $('.seconds').text(ss)
}

function validation() {
    let score = 0
    question_data.forEach(question => {
        let input = $(`input[name=${question.catagery}]:checked`)
        if (input.length != 0) {
            if (input[0].value == question.correct_opt) {
                score += 1
            }
        }
    })
    $.ajax({
        type: 'post',
        url: url,
        data: {
            'user_name': user_name,
            'score': score,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            window.location.href = data.url
        },
        error: function (data) {
            console.log('Error');
        }
    })

}

function showNextCard(e) {
    let currentCard = e.target.closest('.card')
    let nextCard = currentCard.nextElementSibling

    //  Clicking in the start btn
    if ($(currentCard).find('input[type=radio]:checked').length == 0) {
        $(currentCard).find('.err-msg').text('Please choose any one option.')
    }
    else {
        $(currentCard).find('.err-msg').text('')
        // Click in the next btn
        if (nextCard != null) {
            nextCard.classList.remove('d-none')
            scrollTo(0, document.body.scrollHeight)
            nextCard.classList.add('animate')
        }
        if (nextCard == null) {
            validation()
        }
    }
}