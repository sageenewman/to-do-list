from abc import ABC, abstractmethod


class DBClient(ABC):

    @abstractmethod
    def __init__(self, connection_string: str):
        self.connection_string: str = connection_string
        self.client = self.create_client()

    @abstractmethod
    def create_client(self):
        pass
