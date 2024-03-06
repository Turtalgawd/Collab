import database
import bcrypt

from flask import Flask, request, jsonify, render_template, make_response

app = Flask(__name__)

database.init()

def get_username(cookies):
    username = cookies.get('username', '')
    password_hash = cookies.get('password_hash', '')

    if username == '' or password_hash == '':
        return None
    
    if database.account_get(username) != password_hash:
        return None
    
    return username

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/api/notes', methods=['GET', 'POST'])
def api_notes():
    username = get_username(request.cookies)

    if username is None:
        return 'Unauthorized', 401
    
    if request.method == 'GET':
        return jsonify(database.note_get_all(username))

    elif request.method == 'POST':
        name = request.form.get('name', '')
        content = request.form.get('content', '')

        if name == '' or content == '':
            return 'Invalid request', 400

        if name.isalnum() is False:
            return 'Name can only contain alphanumeric characters', 400

        if database.note_get(username, name) is not None:
            return 'Note already exists', 400

        database.note_create(username, name, content)

        return 'Note created'

@app.route('/api/notes/<name>', methods=['GET', 'PUT', 'DELETE'])
def api_notes_name(name):
    username = get_username(request.cookies)

    if username is None:
        return 'Unauthorized', 401
    
    note = database.note_get(username, name)

    if note is None:
        return 'Note not found', 404

    if request.method == 'GET':
        return note

    elif request.method == 'PUT':
        content = request.form.get('content', '')

        if content == '':
            return 'Invalid request', 400

        database.note_update(username, name, content)

        return 'Note updated'

    elif request.method == 'DELETE':
        database.note_delete(username, name)

        return 'Note deleted'
    
@app.route('/api/account', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_account():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if username == '' or password == '':
            return 'Invalid request', 400
        
        if username.isalnum() is False:
            return 'Username can only contain alphanumeric characters', 400
        
        if len(username) <3 or len(username) >16:
            return 'Username must be between 3 and 16 characters', 400
        
        if len(password) <8:
            return 'Password must be at least 8 characters', 400
        
        if database.account_get(username) is not None:
            return 'Username already used', 400
        
        password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        database.account_create(username,password_hash)

        response = make_response('Account created')
        response.set_cookie('username', username)
        response.set_cookie('password_hash', password_hash)

        return response
    
    username = get_username(request.cookies)

    if username is None:
        return 'Unauthorized', 401
    
    if request.method == 'GET':
        return username
    elif request.method == 'PUT':
        password = request.form.get('password', '')

        if password == '':
            return 'Invalid request', 400
        
        if len(password) <8:
            return 'Password must be at least 8 characters', 400
        
        password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        database.account_update(username,password_hash)

        response = make_response('Account updated')
        response.set_cookie('username', username)
        response.set_cookie('password_hash', password_hash)

        return response
    
    elif request.method == 'DELETE':
        database.account_delete(username)

        response = make_response('Account deleted')
        response.delete_cookie('username')
        response.delete_cookie('password_hash')
        
        return response

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if username == '' or password == '':
        return 'Invalid credentials', 401
    
    password_hash = database.account_get(username)

    if password_hash is None:
        return 'Invalid credentials', 401

    verified = bcrypt.checkpw(
        password.encode('utf-8'),
        password_hash.encode('utf-8')
    )

    if verified is False:
        return 'Invalid credentials', 400
    
    response = make_response('Logged in')
    response.set_cookie('username', username)
    response.set_cookie('password_hash', password_hash)

    return response

@app.route('/api/logout', methods=['POST'])
def api_logout():
    response = make_response('Logged out')
    response.delete_cookie('username')
    response.delete_cookie('password_hash')
        
    return response


app.run(host='127.0.0.1', port=8080, debug=True)
