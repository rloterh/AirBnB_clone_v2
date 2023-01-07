#!/usr/bin/python3
""" This is a hello world flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Printing hello HBNB to the home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cee(text):
    """Displays 'c' followed by the value of 'text' """
    return "C {}".format(text.replace('_', " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """ Displays information about python
    default value is 'is cool'
    """
    return "Python {}".format(text.replace('_', " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ displays 'n' is a number if true"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def render(n):
    """ This method renders an html page if n is int"""
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ If 'n' is int, tells if its odd or even"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
