import os
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from dotenv import load_dotenv
import motor.motor_asyncio
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from config.db_config import db_config


# Move to function all code below
load_dotenv()

# Add config file
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGOLINK'])
db = client["codon"]


app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=db_config['mysql'])
Base = declarative_base()
engine = create_engine(db_config['mysql'], echo=True)
Base.metadata.create_all(engine);
