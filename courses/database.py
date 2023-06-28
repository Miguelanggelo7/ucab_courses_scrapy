from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

Base = declarative_base()

load_dotenv()


def db_connect():
    dbName = os.getenv("DB_NAME")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "5432")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{dbName}'
    return create_engine(DATABASE_URL)


def create_table(engine):
    Base.metadata.create_all(engine)


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    type = Column(String)
    career = Column(String)
    university = Column(String)
    startDate = Column(String)
    endDate = Column(String)
    url = Column(String, unique=True)
