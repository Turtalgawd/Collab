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

async function getNotes() {
    var response = await fetch('/api/notes')
    var notes = await response.json()

    return notes
}

async function createNote(name, content) {
    var form = new FormData()
    form.append('name', name)
    form.append('content', content)

    await fetch('/api/notes', {
        method: 'POST',
        body: form
    })

    displayNotes()
}

async function editNote(name) {
    var content = $('#note-content-' + name).val()

    var form = new FormData()
    form.append('content', content)

    await fetch('/api/notes/' + name, {
        method: 'PUT',
        body: form
    })
}

async function deleteNote(name) {
    await fetch('/api/notes/' + name, {
        method: 'DELETE'
    })

    displayNotes()
}

async function displayNotes() {
    var notes = await getNotes()

    var html = ''

    for (var name in notes) {
        var content = notes[name]

        var item = '<div class="accordion-item">\
            <h2 class="accordion-header">\
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-' + name + '">\
                    ' + name + '\
                </button>\
            </h2>\
            <div id="collapse-' + name + '" class="accordion-collapse collapse" data-bs-parent="#note-view">\
                <div class="accordion-body">\
                    <div class="mb-4">\
                        <label for="note-name-' + name + '" class="form-label">Name</label>\
                        <input type="text" class="form-control" id="note-name-' + name + '" value="' + name + '" readonly>\
                    </div>\
                    <div class="mb-4">\
                        <label for="note-content-' + name + '" class="form-label">Content</label>\
                        <textarea class="form-control" id="note-content-' + name + '">' + content + '</textarea>\
                    </div>\
                    <button type="button" class="btn btn-secondary btn-sm me-2" onclick="editNote(\'' + name + '\')">Save edit</button>\
                    <button type="button" class="btn btn-danger btn-sm" onclick="deleteNote(\'' + name + '\')">Delete</button>\
                </div>\
            </div>\
        </div>'

        html += item
    }

    if (html == '') {
        html = '<p class="mb-0">No notes found</p>'
    }

    $('#note-view').html(html)
}

$('#note-create').on('click', function() {
    var name = $('#note-name').val()
    var content = $('#note-content').val()

    if (name.includes(' ')) {
        alert('Name cannot contain spaces')
        return
    }

    $('#note-name').val('')
    $('#note-content').val('')

    createNote(name, content)
})

login().then(function (){
    displayNotes()
})
