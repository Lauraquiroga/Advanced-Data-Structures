from .avl_node import AVlNode
from .base_tree import BaseTree

class AVLTree(BaseTree):
    """
	Class defining the structure of an AVL Tree.
    
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
    
    def rightRotate(self, y):
        pass

    def leftRotate(self, x):
        pass

    def insert_node(self, key):
        pass

    def delete_node(self, key):
        pass

    def insert(self, root, key):
        pass

    def delete(self, root, key):
        pass