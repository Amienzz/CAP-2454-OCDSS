import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import mysql.connector
from mysql.connector import Error

app = FastAPI()

origins = [
    "http://localhost:8000", # Change this to your frontend URL once deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    # Replace with your actual database connection details
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI with MySQL backend!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)