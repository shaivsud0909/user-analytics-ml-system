from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.db import models  

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

#It creates a factory that gives you database sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

Base.metadata.create_all(bind=engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

       