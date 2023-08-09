from sqlalchemy import create_engine , MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv 
from os import environ
load_dotenv()
url = (f"mssql+pyodbc://{environ.get('user')}:{environ.get('password')}@{environ.get('server')}:"
       f"{environ.get('port')}/{environ.get('database')}?driver=ODBC+Driver+17+for+SQL+Server")
engine = create_engine(url)
meta=MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)
conn = engine.connect()
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


