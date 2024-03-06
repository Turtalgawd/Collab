async function login() {
    var username = $('#login-username').val()
    var password = $('#login-password').val()

    var form = new FormData()
    form.append('username', username)
    form.append('password', password)

    var response = await fetch('/api/login', {
        method: 'POST',
        body: form
    })

    if (response.status != 200) {
        alert(await response.text())
        return
    }

    window.location.href = '/'
}

async function register() {
    var username = $('#login-username').val()
    var password = $('#login-password').val()

    var form = new FormData()
    form.append('username', username)
    form.append('password', password)

    var response = await fetch('/api/account', {
        method: 'POST',
        body: form
    })

    if (response.status != 200) {
        alert(await response.text())
        return
    }

    window.location.href = '/'
}

$('#login-login').on('click', function (){
    login()
})

$('#login-register').on('click', function (){
    register()
})