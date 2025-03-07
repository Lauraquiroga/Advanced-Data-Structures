from .rb_node import RBNode
from .base_tree import BaseTree
from .utils import Helper

class RBTree(BaseTree):
    """
	Class defining the structure of a Red-Black Tree.

    Code adapted from: 
    https://www.geeksforgeeks.org/insertion-in-red-black-tree/
    https://www.geeksforgeeks.org/deletion-in-red-black-tree/
    """

    def __init__(self):
        """
        Initializes the Red-Black Tree.
        
        Parameters: 
        None
        
        Return:
        None
        """
        self.root = None
        self.ll_rotation = False
        self.rr_rotation = False
        self.lr_rotation = False
        self.rl_rotation = False

    def show(self):
        """
        Prints the inorder traversal of the tree.

        Parameters:
        None

        Return:
        None
        """
        self.inorder(self.root)

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y                            x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def right_rotate(self, y):
        """
        Performs a right rotation on the given node (y).
        
        Parameters:
        y (RBNode): The node to perform the right rotation on.
        
        Return:
        RBNode: The new root node after the rotation.
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

    def left_rotate(self, x):
        """
        Performs a left rotation on the given node (x).
        
        Parameters:
        x (RBNode): The node to perform the left rotation on.
        
        Return:
        RBNode: The new root node after the rotation.
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

    @Helper.timing_decorator 
    def insert_node(self, key):
        """
        Inserts a new node with the specified key into the Red-Black Tree.
        
        Parameters:
        key (int): The key to be inserted into the tree.
        
        Return:
        None
        """
        # Base case: empty tree
        if self.root is None:
            self.root = RBNode(key)
            self.root.color = 'B'
        else:
            self.root = self.insert(self.root, key)

    def insert(self, root, key):
        """
        Recursively inserts the key into the tree while maintaining the Red-Black Tree properties.
        
        Parameters:
        root (RBNode): The root node of the current subtree.
        key (int): The key to be inserted.
        
        Return:
        RBNode: The root of the modified subtree.
        """
        rr_conflict = False #flag to check RED-RED conflict

        # We have found the key's place on the structure according to the BST order
        if root is None:
            return RBNode(key)
        
        # The key goes on the left tree of the root
        elif key<root.key:
            root.left=self.insert(root.left, key)
            root.left.parent = root
            # Evaluating if there is RED-RED conflict
            if root != self.root: # The root param is not the root of the tree
                if root.color == 'R' and root.left.color == 'R': # 2 consecutive red nodes on the path
                    rr_conflict = True

        # The key goes on the right tree of the root
        else:
            root.right = self.insert(root.right, key)
            root.right.parent = root
            # Evaluating if there is RED-RED conflict
            if root != self.root: # The root param is not the root of the tree
                if root.color == 'R' and root.right.color == 'R': # 2 consecutive red nodes on the path
                    rr_conflict = True
        
        # Perform rotations
        if self.ll_rotation:
            root = self.left_rotate(root)
            root.color = 'B'
            root.left.color = 'R'
            self.ll_rotation = False
        elif self.rr_rotation:
            root = self.right_rotate(root)
            root.color = 'B'
            root.right.color = 'R'
            self.rr_rotation = False
        elif self.rl_rotation:
            root.right = self.right_rotate(root.right)
            root.right.parent = root
            root = self.left_rotate(root)
            root.color = 'B'
            root.left.color = 'R'
            self.rl_rotation = False
        elif self.lr_rotation:
            root.left = self.left_rotate(root.left)
            root.left.parent = root
            root = self.right_rotate(root)
            root.color = 'B'
            root.right.color = 'R'
            self.lr_rotation = False
        
        # Handle RED-RED conflicts
        if rr_conflict:
            # root is a right child
            if root.parent.right == root:
                # root has no left sibling or the sibling is black
                if root.parent.left is None or root.parent.left.color =='B':
                    # root has red left child
                    if root.left is not None and root.left.color == 'R':
                        self.rl_rotation = True

                    # root has red right child
                    elif root.right is not None and root.right.color == 'R':
                        self.ll_rotation = True
                    
                else:
                    root.parent.left.color = 'B'
                    root.color = 'B'
                    if root.parent != self.root:
                        root.parent.color = 'R'

            else:
                if root.parent.right is None or root.parent.right.color == 'B':
                    if root.left is not None and root.left.color == 'R':
                        self.rr_rotation = True
                    elif root.right is not None and root.right.color == 'R':
                        self.lr_rotation= True
                else:
                    root.parent.right.color = 'B'
                    root.color = 'B'
                    if root.parent != self.root:
                        root.parent.color = 'R'

            rr_conflict = False
        return root

    def inorder(self, root):
        """
        Performs an inorder traversal of the tree and prints the key and color of each node.
        
        Parameters:
        root (RBNode): The root node of the current subtree.
        
        Return:
        None
        """
        if root:
            self.inorder(root.left)
            print("key:", root.key, "| color:", root.color, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)