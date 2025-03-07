class AVlNode:
    """
    Class representing a node in an AVL Tree.
    
    Each node contains a key, pointers to its left and right children, and a height value.
    The height is used to balance the tree and maintain the AVL property.
    """

    def __init__(self, key):
        """
        Initializes a new node in the AVL Tree with the specified key.
        
        Parameters:
        key (int): The key to store in the node.
        
        Sets the left and right pointers to None, and initializes the height to 1
        (since a newly created node has height 1, being a leaf node).
        """
        self.key = key  # The key for the node, used for binary search tree property.
        self.left = None  # Pointer to the left child node (initially None).
        self.right = None  # Pointer to the right child node (initially None).
        self.height = 1  # The height of the node, initialized to 1 (leaf node).
