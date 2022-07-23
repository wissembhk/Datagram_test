from database import base
from sqlalchemy import Column, String, Integer


class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    Firstname = Column(String(55), unique=True, index=True)
    Lastname = Column(String(55), unique=True, index=True)
