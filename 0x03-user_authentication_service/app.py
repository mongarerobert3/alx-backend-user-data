#!/usr/bin/env python3
"""Flask app"""

from typing import Union
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth, _generate_uuid
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ Basic Flask app """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Register a user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


def valid_login(email: str, password: str) -> bool:
    """ Check if login is valid """
    try:
        user = AUTH._db.find_user_by(email=email)
        return AUTH.valid_login(email, password)
    except NoResultFound:
        return False



@app.route('/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login a user """
    email = request.form.get('email')
    password = request.form.get('password')
    if valid_login(email, password):
        session_id = create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


def get_user_from_session_id(session_id: str) -> Union[str, None]:
    """ Get user from session id """
    if session_id is None:
        return None
    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        return user
    except NoResultFound:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
