#!/usr/bin/python3
"""
This python script will start a flask web app
"""


from models import storage
from models.state import State
from collections import OrderedDict
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def sesclose(self):
    """close"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def stateslist():
    """This function will send all the states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda states: states.name)
    return render_template('7-states_list.html', stateobj=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
