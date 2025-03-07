class RBNode:
    """
    Class representing a node in a Red-Black Tree.
    
    Each node contains a key, a color, and pointers to its left and right children and its parent.
    By default, the node's color is set to Red ('R') upon initialization.
    """

    def __init__(self, key):
        """
        Initializes a new node in the Red-Black Tree with the specified key.
        
        Parameters:
        key (int): The key to store in the node.
        
        Sets the node's color to Red ('R'), and its left, right, and parent pointers to None.
        """
        self.key = key  # The key for the node.
        self.color = "R"  # By default, new nodes are colored Red ('R').
        self.left = None  # Pointer to the left child node (initially None).
        self.right = None  # Pointer to the right child node (initially None).
        self.parent = None  # Pointer to the parent node (initially None).
