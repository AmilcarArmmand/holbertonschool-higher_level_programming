#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                      argv[2],
                                                                      argv[3]))

    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    session = Session()

    rows = session.query(City, State).filter(City.state_id == State.id)\
                                     .order_by(City.id).all()

    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
