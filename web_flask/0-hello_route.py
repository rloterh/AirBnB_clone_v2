#!/usr/bin/python3
""" This is a hello world flask app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Printing hello HBNB to the home page"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
