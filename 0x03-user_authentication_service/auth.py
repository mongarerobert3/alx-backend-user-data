#!/usr/bin/env python3
"""hash_password module"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ Returns a salted, hashed password, which is a byte string. """
    return hashpw(password.encode('utf-8'), gensalt())
