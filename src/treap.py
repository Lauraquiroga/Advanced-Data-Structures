from .treap_node import TreapNode
from .base_tree import BaseTree
from .utils import Helper

class Treap(BaseTree):
    """
    A Treap (Tree + Heap) is a randomized binary search tree that maintains
    both the BST property and a heap property based on randomly assigned priorities.

    Code adapted from: https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/
    """
    def __init__(self):
        """
        Initializes an empty Treap.
        """
        self.root = None

    def show(self):
        """
        Displays the Treap using an inorder traversal.
        """
        self.inorder(self.root)

    @Helper.timing_decorator 
    def insert_node(self, key):
        """
        Inserts a new node with the given key into the Treap.

        Parameters:
        key (int): The key value to be inserted.

        Returns:
        None
        """
        self.root = self.insert(self.root, key)
    
    def delete_node(self, key):
        """
        Deletes a node with the given key from the Treap.

        Parameters:
        key (int): The key value to be deleted.

        Returns:
        None
        """
        self.root = self.delete(self.root, key)

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y							  x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def right_rotate(self, y):
        """
        Performs a right rotation in the Treap using y as the pivot.

        Parameters:
        y (TreapNode): The node around which the right rotation is performed.

        Returns:
        TreapNode: The new root after rotation.
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Return new root
        return x
        
    def left_rotate(self, x):
        """
        Performs a left rotation in the Treap using x as the pivot.

        Parameters:
        x (TreapNode): The node around which the left rotation is performed.

        Returns:
        TreapNode: The new root after rotation.
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Return new root
        return y

    def insert(self, root, key):
        """
        Recursively inserts a node with the given key into the Treap while maintaining
        both the BST and heap properties.

        Parameters:
        root (TreapNode or None): The root node of the subtree where insertion is performed.
        key (int): The key value to be inserted.

        Returns:
        TreapNode: The root node after insertion.
        """
        # If root is None, create a new node and return it
        if not root:
            return TreapNode(key)
        
        # If key is smaller than root
        if key <= root.key:
            # Insert in left subtree
            root.left = self.insert(root.left, key)
            
            # Fix Heap property if it is violated
            if root.left.priority > root.priority:
                root = self.right_rotate(root)
        else:
            # Insert in right subtree
            root.right = self.insert(root.right, key)
            
            # Fix Heap property if it is violated
            if root.right.priority > root.priority:
                root = self.left_rotate(root)
        return root


    def delete(self, root, key):
        """
        Recursively deletes a node with the given key while preserving Treap properties.

        Parameters:
        root (TreapNode or None): The root node of the subtree where deletion is performed.
        key (int): The key value to be deleted.

        Returns:
        TreapNode or None: The root node after deletion.
        """
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # IF KEY IS AT ROOT
    
            # If left is None
            if not root.left:
                temp = root.right
                root = None
                return temp
    
            # If right is None
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            # If key is at root and both left and right are not None
            elif root.left.priority < root.right.priority:
                root = self.left_rotate(root)
                root.left = self.delete(root.left, key)
            else:
                root = self.right_rotate(root)
                root.right = self.delete(root.right, key)
    
        return root

    def inorder(self, root):
        """
        Performs an inorder traversal of the Treap and prints the keys along with their priorities.

        Parameters:
        root (TreapNode or None): The root node of the subtree to traverse.

        Returns:
        None
        """
        if root:
            self.inorder(root.left)
            print("key:", root.key, "| priority:", root.priority, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)