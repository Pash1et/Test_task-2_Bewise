from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import (POSTGRES_USER, POSTGRES_PASSWORD,
                    DB_HOST, DB_PORT, POSTGRES_DB)


DB_URL = (f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
          f'{DB_HOST}:{DB_PORT}/{POSTGRES_DB}')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
