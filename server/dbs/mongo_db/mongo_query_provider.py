from dbs.query_provider.abstract_query_provider import QueryProvider


class MongoQueryProvider(QueryProvider):

    def __init__(self):
        super().__init__()
