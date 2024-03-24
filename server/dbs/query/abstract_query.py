from abc import ABC, abstractmethod


class Query(ABC):

    @abstractmethod
    def __init__(self, r):
        # self.client = db.client(connection_string)
        pass
