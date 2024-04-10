import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('temphtmlpage.html')

@app.route('/info')
def info():
    return flask.render_template('bryan_portfolio.html')


app.run(debug=True)