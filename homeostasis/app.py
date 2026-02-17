from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from dotenv import load_dotenv

from config.db_config import db_config


# Move to function all code below
load_dotenv()

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=db_config['mysql'])

