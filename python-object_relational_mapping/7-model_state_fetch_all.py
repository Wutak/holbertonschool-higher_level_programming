#!/usr/bin/python3
"""class definition"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
