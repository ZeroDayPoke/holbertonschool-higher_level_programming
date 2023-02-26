#!/usr/bin/python3
"""test comment"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    toggle = False
    for state in session.query(State) \
            .filter(State.name.like('%a%')).order_by(State.id):
        session.delete(state)
        toggle = True
    if toggle:
        session.commit()
    session.close()
