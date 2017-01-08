import flask
from flask import render_template
import sunpy
import datetime

import sunpy.lightcurve as lc
from sunpy.time import TimeRange, parse_time

DEFAULT_TR = TimeRange(['2011-06-07 00:00', '2011-06-07 12:00'])
goes = lc.GOESLightCurve.create(DEFAULT_TR)


app = flask.Flask(__name__)

@app.route('/')
def index():
    text = sunpy.__version__ + '\n' + goes.data.describe()
    current_time = str(datetime.datetime.now())
    return render_template('index.html', text=text, 
current_time=current_time)

if __name__ == '__main__':
    print(__doc__)
    app.run()
