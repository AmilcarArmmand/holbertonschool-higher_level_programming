#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                      argv[2],
                                                                      argv[3]),
                          pool_pre_ping=True)

    Base.metadata.create_all(engin)

    Session = sessionmaker(bind=engin)
    session = Session()
    my_state = State(name='California')
    my_city = City(name="San Francisco", state_id=my_state.id)
    my_state.cities.append(my_city)
    session.add(my_state)
    session.commit()
    session.close()
