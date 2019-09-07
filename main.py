#! /usr/bin/python
#! -*- encoding: utf-8 -*-

import json
import random
import time
import itertools
from datetime import datetime

from flask import Flask, Response, render_template, jsonify, current_app

application = Flask(__name__, template_folder=".")

random.seed()  # Initialize the random number generator

@application.route('/')
def index():
    return render_template('./index.html')


@application.route('/chart-data')
def chart_data():
    def gen():
        for i, c in enumerate(itertools.cycle('\|/-')):
            yield "data: %s\n\n" % (str(random.random()*10))
            time.sleep(.1)
    return Response(gen(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)

