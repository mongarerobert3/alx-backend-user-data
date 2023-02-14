#!/usr/bin/env python3
"""Users database model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    """User class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email, hashed_password):
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self):
        return "<User(email='%s', hashed_password='%s')>" % (
            self.email, self.hashed_password)
