import flask
from flask import render_template
import sunpy
import datetime

app = flask.Flask(__name__)

@app.route('/')
def index():
    text = sunpy.__version__
    current_time = str(datetime.datetime.now())
    return render_template('index.html', text=text, 
current_time=current_time)

if __name__ == '__main__':
    print(__doc__)
    app.run()
