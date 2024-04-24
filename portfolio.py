import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('temphtmlpage.html')

@app.route('/<name>')
def info(name):
    return flask.render_template(f'{name}_portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)