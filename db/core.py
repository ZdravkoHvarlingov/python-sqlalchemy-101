from curses import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = 'sqlite:///database.db'


engine = create_engine(CONNECTION_STRING, echo=True)
Base = declarative_base(engine)
Session = sessionmaker(engine)
