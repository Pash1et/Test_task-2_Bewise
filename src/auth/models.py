from sqlalchemy import Column, String, Integer
from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    UUID = Column(String, nullable=False)
