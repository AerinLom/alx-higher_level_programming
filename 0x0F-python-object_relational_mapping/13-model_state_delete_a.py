#!/usr/bin/python3
"""
Updates the State object with the specified id from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db_url = (
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database_name))
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    del_states = db_session.query(State).filter(State.name.like('%a%')).all()

    for state in del_states:
        db_session.delete(state)

    db_session.commit()
