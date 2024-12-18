from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from database import Base

class User(Base, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, name, email, senha):
        self.name = name
        self.email = email
        self.password = generate_password_hash(senha)

class Cavalo(Base):
    __tablename__ = 'horses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    race: Mapped[str] = mapped_column(String(64), nullable=True)

    def __init__(self, name, race):
        self.name = name
        self.race = race
