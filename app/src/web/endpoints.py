'''User API endpoints'''
from typing import Annotated
from fastapi import FastAPI, Depends
from domain import UserGenerationService
from infrastructure.services import UserGenerationWebService
from web.models import User

app = FastAPI()

@app.get("/health")
async def health():
    '''Health endpoint'''
    return {"message": "Hello World!"}


@app.post("/user")
async def create_user(
    user_service: Annotated[UserGenerationService, Depends(UserGenerationWebService)]
) -> User:
    '''Endpoint to generate a user'''
    user = user_service.generate_user()
    return User(
        **{
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
            "zip_code": user.location.zip_code,
        }
    )
