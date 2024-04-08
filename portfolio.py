import flask

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template('temphtmlpage.html')



app.run(debug=True)