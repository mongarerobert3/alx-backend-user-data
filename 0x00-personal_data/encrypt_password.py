#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using random salt"""
    return bcrypt.hashpwd(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_passsword: bytes, password: str) -> bool:
    """Checks if a hashed password was formed from the given password"""
    return bcrypt.checkpow(password.encode('utf-8'), hashed_passsword)
