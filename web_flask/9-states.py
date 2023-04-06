#!/usr/bin/python3
"""This python script will start a flask web app"""


from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv
app = Flask(__name__)
env = getenv('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def teardown_close(self):
    "Closses sqlalchemy session"
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_list(id=None):
    """Returns a HTML with states list"""
    state_list = storage.all(State).values()
    if not id:
        return render_template('9-states.html', st_list=state_list, status=1)
    for state in state_list:
        if state.id == id:
            return render_template('9-states.html', st_list=[state], status=2)
    return render_template('9-states.html', st_list=None, status=0)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")