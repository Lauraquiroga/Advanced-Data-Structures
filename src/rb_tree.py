from .rb_node import RBNode
from .base_tree import BaseTree

class RBTree(BaseTree):
    """
	Class defining the structure of a Red-Black Tree.

    Code adapted from: 
    https://www.geeksforgeeks.org/insertion-in-red-black-tree/
    """

    def __init__(self):
        self.root = None
        self.ll_rotation = False
        self.rr_rotation = False
        self.lr_rotation = False
        self.rl_rotation = False

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y                            x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def rightRotate(self, y):
        """
        Perform Right Rotation
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2

        # Fix parents
        y.parent = x
        if T2 is not None:
            T2.parent = y
        
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

        # Fix parents
        x.parent = y
        if T2 is not None:
            T2.parent = x
        
        # Return new root
        return y

    def insert_node(self, key):
        # Base case: empty tree
        if self.root is None:
            self.root = self.Node(key)
            self.root.colour = 'B'
        else:
            self.root = self.insert(self.root, key)

    def delete_node(self, key):
        pass

    def insert(self, root, key):
        pass

    def delete(self, root, key):
        pass