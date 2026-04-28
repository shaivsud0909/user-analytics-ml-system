from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
 

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL,echo=True)

#It creates a factory that gives you database sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# tracks all models (User, etc.)
# collects metadata
# used to create tables
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

