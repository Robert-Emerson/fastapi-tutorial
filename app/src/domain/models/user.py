from dataclasses import field, dataclass
import datetime
import uuid

@dataclass
class LocationEntity:
    address_line_one: str = ''
    address_line_two: str = ''
    city: str = ''
    state_or_province: str = ''
    country: str = ''
    zip_code: str = ''
    latitude: float = None
    longitude: float = None

@dataclass
class UserModel:
    first_name: str = ''
    last_name: str = ''
    birthday: datetime.date = None
    phone: str = ''
    email: str = ''
    location: LocationEntity = None
    id: str = field(default_factory=lambda: uuid.uuid4().hex)