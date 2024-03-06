async function login() {
    var response = await fetch('/api/account')

    if (response.status != 200) {
        window.location.href = '/login'
        return
    }

    var username = await response.text()

    $('#nav-username').text(username)
}

async function logout() {
    var response = await fetch('/api/logout', {
        method: 'POST'
    })

    alert(await response.text())

    window.location.href = '/login'
}

async function changePassword() {
    var password = $('#account-password').val()

    $('#account-password').val('')

    var form = new FormData()
    form.append('password',password)

    var response = await fetch('/api/account', {
        method: 'PUT',
        body: form
    })

    alert(await response.text())
}

async function deleteAccount() {
    var confirmed = confirm('Are you sure you want to delete your account?')

    if (!confirmed) return

    var response = await fetch('/api/account', {
        method: 'DELETE'
    })

    alert(await response.text())

    window.location.href = '/login'
}

$('#account-change').on('click', function(){
    changePassword()
})

$('#account-delete').on('click', function(){
    deleteAccount()
})

$('#account-logout').on('click', function(){
    logout()
})