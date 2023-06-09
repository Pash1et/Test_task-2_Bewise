from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (DB_HOST, DB_PORT, POSTGRES_DB, POSTGRES_PASSWORD,
                    POSTGRES_USER)

DB_URL = (f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
          f'{DB_HOST}:{DB_PORT}/{POSTGRES_DB}')

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
