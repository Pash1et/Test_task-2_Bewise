from sqlalchemy import Column, Integer, String

from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    UUID = Column(String, nullable=False)
