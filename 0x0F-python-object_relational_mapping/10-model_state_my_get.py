#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
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
    Session = sessionmaker(bind=engin)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).order_by(
        State.id).first()
    if state:
        print(str(state.id))
    else:
        print("Not found")

    session.close()
