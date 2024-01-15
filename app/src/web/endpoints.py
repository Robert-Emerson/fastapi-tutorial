from typing import Annotated
from fastapi import FastAPI, Depends
from domain.services.user_generation_service import UserGenerationService
from infrastructure.services.user_generation_web_service import UserGenerationWebService
from web.user import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/user")
async def create_user(
    user_service: Annotated[UserGenerationService, Depends(UserGenerationWebService)]
) -> User:
    user = user_service.generate_user()
    return User(
        **{
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
            "zip_code": user.location.zip_code,
        }
    )
