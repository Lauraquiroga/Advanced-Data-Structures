from abc import ABC, abstractmethod
from .utils import Helper

class BaseTree(ABC):
    """
    Abstract base class defining the common interface for a tree structure.
    This class uses abstract methods to be implemented by subclasses such as AVLTree.
    """

    @abstractmethod
    def show(self, key):
        """
        Abstract method to display the tree, to be implemented by subclasses.
        
        Parameters:
        key (int): The key to display (usage may vary by subclass).
        
        Return:
        None
        """
        pass

    @abstractmethod
    def insert_node(self, key):
        """
        Abstract method to insert a new node into the tree, to be implemented by subclasses.
        
        Parameters:
        key (int): The key to be inserted.
        
        Return:
        None
        """
        pass

    @abstractmethod
    def right_rotate(self, y):
        """
        Abstract method to perform a right rotation on the subtree rooted at the given node (y),
        to be implemented by subclasses.
        
        Parameters:
        y (Node): The node to perform right rotation on.
        
        Return:
        Node: The new root node after the right rotation.
        """
        pass

    @abstractmethod
    def left_rotate(self, x):
        """
        Abstract method to perform a left rotation on the subtree rooted at the given node (x),
        to be implemented by subclasses.
        
        Parameters:
        x (Node): The node to perform left rotation on.
        
        Return:
        Node: The new root node after the left rotation.
        """
        pass

    @Helper.timing_decorator 
    def search_key(self, key):
        """
        Searches for a node with the given key in the tree.
        This method calls the recursive `search` method and returns the result.

        Parameters:
        key (int): The key to search for in the tree.
        
        Return:
        bool: True if the key is found, False if not.
        """
        return self.search(self.root, key)
    
    def search(self, root, key):
        """
        Perform a Binary Search Tree (BST) search to find the node with the specified key.
        
        Parameters:
        root (Node): The current node to search from.
        key (int): The key to search for.
        
        Return:
        bool: True if the key is found, False if the search reaches a leaf node (None).
        """
        # If the current node is None, the key isn't found
        if not root:
            return False
        # If the key is found at the current node, return True
        elif root.key == key:
            return True
        
        # If the key is greater than the current node's key, search the right subtree
        if root.key < key:
            return self.search(root.right, key)
        
        # If the key is smaller than the current node's key, search the left subtree
        return self.search(root.left, key)
