'''Models and domain service abstractions'''

from abc import ABC, abstractmethod
from dataclasses import field, dataclass
import datetime
import uuid

@dataclass
class LocationEntity:
    '''Data class for location information'''
    address_line_one: str = ""
    address_line_two: str = ""
    city: str = ""
    state_or_province: str = ""
    country: str = ""
    zip_code: str = ""
    latitude: float = None
    longitude: float = None

@dataclass
class UserModel:
    '''Domain model for a user'''
    first_name: str = ""
    last_name: str = ""
    birthday: datetime.date = None
    phone: str = ""
    email: str = ""
    location: LocationEntity = None
    id: str = field(default_factory=lambda: uuid.uuid4().hex)


class UserGenerationService(ABC):
    '''Abstract class containing methods for generating users'''
    @classmethod
    def generate_user(cls) -> UserModel:
        '''Abstract method to generate a user model from some external service'''
        raise NotImplementedError
