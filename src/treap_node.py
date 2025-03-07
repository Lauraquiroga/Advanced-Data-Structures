import random 

class TreapNode:
    """
    Class representing a node in a Treap (a randomized binary search tree).
    
    Each node contains a key, a priority (randomly assigned), and pointers to its left and right children.
    The priority helps maintain the heap property of the Treap.
    """

    def __init__(self, key):
        """
        Initializes a new node in the Treap with the specified key and a random priority.
        
        Parameters:
        key (int): The key to store in the node.
        
        Sets the node's priority to a random value between 0 and 99, and initializes
        the left and right pointers to None.
        """
        self.key = key  # The key for the node, used for binary search tree property.
        self.priority = random.randint(0, 99)  # Random priority to maintain heap property.
        self.left = None  # Pointer to the left child node (initially None).
        self.right = None  # Pointer to the right child node (initially None).