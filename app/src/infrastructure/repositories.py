from abc import ABC, abstractmethod
import os
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

username = os.environ.get("POSTGRES_USERNAME")
password = os.environ.get("POSTGRES_PASSWORD")
database = os.environ.get("POSTGRES_DATABASE")
instance = os.environ.get("POSTGRES_INSTANCE")

connection_string = f'postgresql://{username}:{password}@{instance}/{database}'
engine = create_engine(connection_string, echo=True)

class RepositoryBase[T](ABC):
    # pylint: disable=undefined-variable

    @abstractmethod
    def get(self, entityId: Any) -> T:
        raise NotImplementedError

    @abstractmethod
    def find(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, entity: T) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entityId: Any) -> bool:
        raise NotImplementedError

class DatabaseRepositoryBase[T](RepositoryBase):
    # pylint: disable=undefined-variable
    def get(self, entityId: Any) -> T:
        with Session(engine) as session:
            return session.get(entityId)