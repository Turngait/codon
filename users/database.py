from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from config.db_config import db_config


# TODO: To make as a class
Base = declarative_base()
engine = create_engine(db_config['mysql'], echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine);

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()