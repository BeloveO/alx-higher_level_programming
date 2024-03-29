#!/usr/bin/python3
"""
Write a python file that contains the class definition of a
State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Links to the MySQL table states, class attribute id
    class attribute name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
