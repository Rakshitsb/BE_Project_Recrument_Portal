from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("DATABASE_URL")

if not MONGO_URL:
    raise ValueError("DATABASE_URL not found in environment variables")

client = MongoClient(MONGO_URL)

db = client.hr_portal

user_collection = db.users
job_collection = db.jobs
application_collection = db.applications

print("Database connected successfully")

