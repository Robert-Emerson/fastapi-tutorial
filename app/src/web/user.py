from dataclasses import dataclass


@dataclass
class User:
    """DTO representing a user"""

    first_name: str = ""
    last_name: str = ""
    id: str = ""
    zip_code: str = ""
