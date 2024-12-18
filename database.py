from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine('sqlite:///database.db', echo=True)

class Base(DeclarativeBase):
    pass

session = Session(bind=engine)  # Sessão local configurada
