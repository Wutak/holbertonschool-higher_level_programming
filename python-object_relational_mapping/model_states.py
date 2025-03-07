#!/usr/bin/python3
"""class definition"""
Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
