from dbs.mongo_db.exceptions.mongo_exceptions import CollectionNoneError, DBNoneError


def none_value_validation(func):
    def wrapper(self, *args, **kwargs):
        if self.db is None:
            raise DBNoneError
        if self.collection is None:
            raise CollectionNoneError
        return func(self, *args, **kwargs)

    return wrapper
