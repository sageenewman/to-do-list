from typing import Any

from dbs.db_client.abstract_client import DBClient
from dbs.mongo_db.validator.validation import none_value_validation
from dbs.query_executor.abstract_query_executor import QueryExecutor


class MongoQueryExecutor(QueryExecutor):

    def __init__(self, db_client: DBClient):
        super().__init__(db_client)
        self.db: str | None = None
        self.collection: str | None = None

    def set_db(self, db: str):
        self.db = db

    def set_collection(self, collection: str):
        self.collection = collection

    @none_value_validation
    def create(self, document_to_insert: Any):
        self.client[self.db][self.collection].insert_one(document_to_insert)

    @none_value_validation
    def update(self):
        pass

    @none_value_validation
    def get(self):
        pass

    @none_value_validation
    def delete(self):
        pass
