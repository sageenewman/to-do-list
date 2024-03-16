from abc import ABC, abstractmethod

from dbs.db_client.abstract_client import DBClient


class QueryExecutor(ABC):

    def __init__(self, db_client: DBClient):
        self.client = db_client

    @abstractmethod
    def create(self, query):
        pass

    @abstractmethod
    def get(self, query):
        pass

    @abstractmethod
    def update(self, query):
        pass

    @abstractmethod
    def delete(self, query):
        pass
