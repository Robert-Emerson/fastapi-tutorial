'''User API endpoints'''
from typing import Annotated
from fastapi import APIRouter,Depends

from src.users.models import User
from src.users.schemas import UserGenerationService
from src.users.services import UserGenerationWebService

router = APIRouter(
    prefix="/user",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_user(
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


@router.get("/user/{id}")
def get_user() -> User:
    '''Endpoint to return a user'''
    return User(
        **{
            "first_name": "user.first_name",
            "last_name": "user.last_name",
            "id": "user.id",
            "zip_code": "user.location.zip_code",
        }
    )

