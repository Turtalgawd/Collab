import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

def init():
    cur.execute('CREATE TABLE IF NOT EXISTS notes (username TEXT, name TEXT, content TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS accounts (username TEXT, password TEXT)')
    con.commit()

def note_get_all(username):
    cur.execute('SELECT name, content FROM notes WHERE username = ?', (username,))
    return dict(cur.fetchall())

def note_get(username, name):
    cur.execute('SELECT content FROM notes WHERE username = ? AND name = ?', (username, name))
    res = cur.fetchone()
    if res is None:
        return None
    return res[0]

def note_create(username, name, content):
    cur.execute('INSERT INTO notes VALUES (?, ?, ?)', (username, name, content))
    con.commit()

def note_update(username, name, content):
    cur.execute('UPDATE notes SET content = ? WHERE name = ? AND username = ?', (content, name, username))
    con.commit()

def note_delete(username, name):
    cur.execute('DELETE FROM notes WHERE username = ? AND name = ?', (username, name))
    con.commit()

def account_get_all():
    cur.execute('SELECT * FROM accounts')
    return dict(cur.fetchall())

def account_get(username):
    cur.execute('SELECT password FROM accounts WHERE username = ?', (username,))
    res = cur.fetchone()
    if res is None:
        return None
    return res[0]

def account_create(username, password):
    cur.execute('INSERT INTO accounts VALUES (?, ?)', (username, password))
    con.commit()

def account_update(username, password):
    cur.execute('UPDATE accounts SET password = ? WHERE username = ?', (password, username,))
    con.commit()

def account_delete(username):
    cur.execute('DELETE FROM notes WHERE username = ?', (username,))
    cur.execute('DELETE FROM accounts WHERE username = ?', (username,))
    con.commit()