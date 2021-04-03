#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Session engine"""
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                          format(sys.argv[1], sys.argv[2], sys.argv[3]),
                          pool_pre_ping=True)

    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    session = Session()
    rows = session.query(State).all()
    for state in rows:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
