from abc import ABC, abstractmethod

class BaseTree(ABC):
    @abstractmethod
    def insert_node(self, key):
        pass

    @abstractmethod
    def rightRotate(self, y):
        pass

    @abstractmethod
    def leftRotate(self, x):
        pass

    def search_key(self, key):
        """
        Search for a node by a given key
        
        Parameters:
        
        Return:
        """
        print(f"Searching key={key}")
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