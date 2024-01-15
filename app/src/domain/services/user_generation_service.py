from abc import ABC, abstractmethod

from domain.models.user import UserModel


class UserGenerationService(ABC):
    @abstractmethod
    def generate_user(self) -> UserModel:
        raise NotImplementedError
