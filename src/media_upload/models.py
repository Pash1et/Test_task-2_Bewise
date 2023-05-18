from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String

from src.database import Base


class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True, index=True)
    author = Column(ForeignKey('user.id'))
    UUID = Column(String, nullable=False)
    file = Column(LargeBinary, nullable=False)
