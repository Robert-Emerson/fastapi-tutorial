from dataclasses import dataclass
from domain.models.user import UserModel

@dataclass
class User:
    first_name: str = ''
    last_name: str = ''
    id: str = ''
    zip_code: str = ''