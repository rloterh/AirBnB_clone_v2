#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a flask app
    listens to 0.0.0.0:5000
    
"""
from models import storage
from flask import Flask
from flask import render_template
=======
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

>>>>>>> 36d13a52715d4546610c45da493c766ab08e732a

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
<<<<<<< HEAD
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
=======
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
>>>>>>> 36d13a52715d4546610c45da493c766ab08e732a
    storage.close()


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 36d13a52715d4546610c45da493c766ab08e732a
