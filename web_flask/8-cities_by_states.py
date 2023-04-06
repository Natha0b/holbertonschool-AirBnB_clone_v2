#!/usr/bin/python3
"""This python script will start a flask web app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def sesclose(self):
    """close"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states_and_cities():
    """This function will send all the states"""
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
