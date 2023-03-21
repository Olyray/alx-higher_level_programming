#!/usr/bin/python3
"""
Prints the first item in the States table
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_in_var = (session.query(State).filter(State.name.like(sys.argv[4]))
                    .order_by(State.id).all())
    if not state_in_var:
        print("Not found")
    else:
        print(state_in_var[0].id)
