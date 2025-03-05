from .avl_node import AVlNode
from .base_tree import BaseTree

class AVLTree(BaseTree):
    """
	Class defining the structure of an AVL Tree.
    
    Code adapted from: https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
    """

    def __init__(self):
        self.root = None

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y							  x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def show(self):
        self.inorder(self.root)

    def height(self, node):
        """
        Calculates the height of the tree from the given node
        (distance to the leaf)
        """
        if not node:
            return 0
        return node.height
    
    def rightRotate(self, y):
        """
        Perform Right Rotation
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        
        # Return new root
        return x

    def leftRotate(self, x):
        """
        Perform Left Rotation
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        
        # Return new root
        return y

    def insert_node(self, key):
        pass

    def insert(self, root, key):
        pass

    def inorder(self, root):
        """
        """
        if root:
            self.inorder(root.left)
            print("key:", root.key, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)