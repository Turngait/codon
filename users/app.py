import os
from fastapi import FastAPI
from dotenv import load_dotenv
import motor.motor_asyncio

# Move to function all code below
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGOLINK'])
db = client["codon"]

app = FastAPI()






