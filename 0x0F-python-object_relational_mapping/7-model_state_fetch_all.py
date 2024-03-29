#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                      argv[2],
                                                                      argv[3]))

    Base.metadata.create_all(engin)
    Session = sessionmaker()   # Session = sessionmaker(bind=engin) truncated
    Session.configure(bind=engin)

    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
