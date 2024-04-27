#!/usr/bin/env python3
"""
Module for task 0
"""


from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    """task 0 route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
