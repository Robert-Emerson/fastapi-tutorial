from typing import Annotated
from fastapi import FastAPI

from src.users import router as users

app = FastAPI()

app.include_router(users.router)

@app.get("/health")
def health():
    '''Health endpoint'''
    return {"message": "Hello World!"}