from abc import ABC, abstractmethod
from .utils import Helper

class BaseTree(ABC):
    @abstractmethod
    def show(self, key):
        pass

    @abstractmethod
    def insert_node(self, key):
        pass

    @abstractmethod
    def right_rotate(self, y):
        pass

    @abstractmethod
    def left_rotate(self, x):
        pass

    @Helper.timing_decorator 
    def search_key(self, key):
        """
        Search for a node by a given key
        
        Parameters:
        
        Return:
        """
        return self.search(self.root, key)
    
    def search(self, root, key):
        """
        Perform BST search.

        Parameters:

        Return:

        """
        # Empty (root is None)
        if not root:
            return False
        # Key is present at root
        elif root.key == key:
            return True
        
        # Key is greater than root's key
        if root.key < key:
            return self.search(root.right, key)
        
        # Key is smaller than root's key
        return self.search(root.left, key)