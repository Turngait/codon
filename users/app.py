import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
import motor.motor_asyncio
from config.db_config import db_config



# Move to function all code below
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGOLINK'])

db = client["codon"]

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=db_config['mysql'])
