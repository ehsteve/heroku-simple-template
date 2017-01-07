import flask
from flask import render_template
import sunpy

app = flask.Flask(__name__)

@app.route('/')
def index():
    text = sunpy.__version__
    return render_template('index.html', text=text)

if __name__ == '__main__':
    print(__doc__)
    app.run()
