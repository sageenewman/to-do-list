import pymongo

from dbs.db_client.abstract_client import DBClient


class MongoClient(DBClient):

    def __init__(self, connection_string: str):
        super().__init__(connection_string)

    def create_client(self):
        return pymongo.MongoClient(self.connection_string)
