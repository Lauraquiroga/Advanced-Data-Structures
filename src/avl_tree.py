from .avl_node import AVlNode
from .base_tree import BaseTree
from .utils import Helper

class AVLTree(BaseTree):
    """
    Class defining the structure of an AVL Tree, which is a self-balancing binary search tree.
    
    Code adapted from: 
    https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
    """

    def __init__(self):
        """
        Initializes the AVL Tree with an empty root.

        Parameters:
        None
        
        Return:
        None
        """
        self.root = None

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y							  x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def show(self):
        """
        Prints the inorder traversal of the tree, which shows the nodes in ascending order.

        Parameters:
        None

        Return:
        None
        """
        self.inorder(self.root)

    def height(self, node):
        """
        Calculates the height of the tree from the given node (distance to the leaf).
        
        Parameters:
        node (AVlNode): The node from which the height needs to be calculated.
        
        Return:
        int: The height of the node, 0 if the node is None.
        """
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        """
        Gets the balance factor of the given node, which is the difference between 
        the height of its left and right subtrees.
        
        Parameters:
        node (AVlNode): The node for which the balance factor is calculated.
        
        Return:
        int: The balance factor of the node (height(left) - height(right)).
        """
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, y):
        """
        Performs a right rotation on the subtree rooted at the given node (y).
        
        Parameters:
        y (AVlNode): The node around which the right rotation occurs.
        
        Return:
        AVlNode: The new root node after the right rotation.
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
        Performs a left rotation on the subtree rooted at the given node (x).
        
        Parameters:
        x (AVlNode): The node around which the left rotation occurs.
        
        Return:
        AVlNode: The new root node after the left rotation.
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

    @Helper.timing_decorator 
    def insert_node(self, key):
        """
        Interface function called from outside the class to insert a new node in the tree.
        
        Parameters:
        key (int): The key to be inserted into the tree.
        
        Return:
        None
        """
        # Base case: empty tree
        if self.root is None:
            self.root = AVlNode(key)
        else:
            self.root = self.insert(self.root, key)

    def insert(self, root, key):
        """
        Recursive function to insert a new key in the subtree rooted at 'root'.
        After insertion, it ensures the AVL tree remains balanced by checking
        the balance factor and performing necessary rotations.
        
        Parameters:
        root (AVlNode): The root node of the subtree where the key will be inserted.
        key (int): The key to be inserted into the subtree.
        
        Return:
        AVlNode: The root node of the modified subtree after insertion.
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
        Inorder traversal of the AVL Tree. It prints the keys and heights of the nodes.
        
        Parameters:
        root (AVlNode): The root node of the current subtree being traversed.
        
        Return:
        None
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