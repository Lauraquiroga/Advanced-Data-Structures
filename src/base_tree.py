from abc import ABC, abstractmethod

class BaseTree(ABC):
    @abstractmethod
    def insert_node(self, key):
        pass

    @abstractmethod
    def delete_node(self, key):
        pass

    @abstractmethod
    def search_key(self, key):
        pass