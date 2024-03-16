class DBNoneError(Exception):
    def __init__(self, message="DB cannot be None"):
        self.message = message
        super().__init__(self.message)


class CollectionNoneError(Exception):
    def __init__(self, message="collection cannot be None"):
        self.message = message
        super().__init__(self.message)
