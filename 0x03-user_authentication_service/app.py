#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ Basic Flask app """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
