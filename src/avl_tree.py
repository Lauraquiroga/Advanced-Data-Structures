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
    
    def get_balance(self, node):
        """
        Get balance factor of given node
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, y):
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

    def left_rotate(self, x):
        """
        Perform Left Rotation
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        # Return new root
        return y

    def insert_node(self, key):
        """
        Function called from outside the class (interface?) to insert a new node on the tree
        """
        # Base case: empty tree
        if self.root is None:
            self.root = AVlNode(key)
        else:
            self.root = self.insert(self.root, key)

    def insert(self, root, key):
        """
        Recursive function to insert a key in the subtree rooted at 'root'
        """
        # We have found the key's place on the structure according to the BST order
        if root is None:
            return AVlNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Equal keys are not allowed in BST
            return root

        # Update height of this ancestor node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Get the balance factor of this ancestor node
        balance = self.get_balance(root)

        # If this node becomes unbalanced, 
        # then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) node pointer
        return root
        

    def inorder(self, root):
        """
        """
        if root:
            self.inorder(root.left)
            print("key:", root.key, "| height:", root.height, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)