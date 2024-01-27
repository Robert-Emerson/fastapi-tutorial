'''Concrete implementations of domain services'''

from typing import Any
import datetime
import requests
from pydantic import BaseModel
from src.users.schemas import UserModel, UserGenerationService, LocationEntity

class _UserServiceModel(BaseModel):
    name: dict[str, str]
    location: dict[str, Any | dict[str, Any]]
    dob: dict[str, Any]
    phone: str
    email: str


class UserGenerationWebService(UserGenerationService):
    @classmethod
    def generate_user(cls) -> UserModel:

        # TODO: implement retry logic (maybe decorator for this?)
        response = requests.get("https://randomuser.me/api/")
        service_user = _UserServiceModel(**response.json()["results"][0])
        return cls.__map_service_user_to_domain(service_user)

    @staticmethod
    def __map_service_user_to_domain(
        service_user: _UserServiceModel,
    ) -> UserModel:
        return UserModel(
            first_name=service_user.name["first"],
            last_name=service_user.name["last"],
            birthday=datetime.datetime.fromisoformat(service_user.dob["date"]).date(),
            phone=service_user.phone,
            email=service_user.email,
            location=LocationEntity(
                address_line_one=str(service_user.location["street"]["number"])
                + " "
                + service_user.location["street"]["name"],
                city=service_user.location["city"],
                state_or_province=service_user.location["state"],
                country=service_user.location["country"],
                zip_code=str(service_user.location["postcode"]),
                latitude=service_user.location["coordinates"]["latitude"],
                longitude=service_user.location["coordinates"]["longitude"],
            ),
        )
