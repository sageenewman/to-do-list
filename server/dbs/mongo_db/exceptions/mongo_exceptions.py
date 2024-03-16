class DBNoneError(Exception):
    def __init__(self, message="DB cannot be None,pleas set db"):
        self.message = message
        super().__init__(self.message)


class CollectionNoneError(Exception):
    def __init__(self, message="collection cannot be None,pleas set collection"):
        self.message = message
        super().__init__(self.message)
