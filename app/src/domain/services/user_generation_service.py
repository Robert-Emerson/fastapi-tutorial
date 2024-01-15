from abc import ABC, abstractmethod

class UserGenerationService(ABC):
    @abstractmethod
    def generate_user(self):
        raise NotImplementedError