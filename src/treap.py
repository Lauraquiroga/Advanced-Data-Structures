from .treap_node import TreapNode
from .base_tree import BaseTree

class Treap(BaseTree):
    """
	Code adapted from: https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/
    
    """
    def __init__(self):
        self.root = None

    def show_treap(self):
        self.inorder(self.root)

    def insert_node(self, key):
        print(f"Inserting key={key}")
        self.root = self.insert(self.root, key)
    
    def delete_node(self, key):
        print(f"Deleting key={key}")
        self.root = self.delete(self.root, key)

    def search_key(self, key):
        """
        Search for a node by a given key
        
        Parameters:
        
        Return:
        """
        print(f"Searching key={key}")
        return self.search(self.root, key)

    # T1, T2 and T3 are subtrees of the tree rooted with y
    # (on left side) or x (on right side)
    #			 y							  x
    #			 / \	 Right Rotation		 / \
    #			 x T3    – – – – – – – >    T1  y
    #			/ \	    < - - - - - - -		   / \
    #		   T1 T2	  Left Rotation	      T2 T3 */
    
    def rightRotate(self, y):
        """
        """
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Return new root
        return x
        
    def leftRotate(self, x):
        """
        """
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Return new root
        return y

    def insert(self, root, key):
        # If root is None, create a new node and return it
        if not root:
            return TreapNode(key)
        
        # If key is smaller than root
        if key <= root.key:
            # Insert in left subtree
            root.left = self.insert(root.left, key)
            
            # Fix Heap property if it is violated
            if root.left.priority > root.priority:
                root = self.rightRotate(root)
        else:
            # Insert in right subtree
            root.right = self.insert(root.right, key)
            
            # Fix Heap property if it is violated
            if root.right.priority > root.priority:
                root = self.leftRotate(root)
        return root

    def delete(self, root, key):
        """
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
                root = self.leftRotate(root)
                root.left = self.delete(root.left, key)
            else:
                root = self.rightRotate(root)
                root.right = self.delete(root.right, key)
    
        return root

    def search(self, root, key):
        """
        """
        # Empty (root is None)
        if not root:
            return False
        # Key is present at root
        elif root.key == key:
            return True
        
        # Key is greater than root's key
        if root.key < key:
            return self.search(root.right, key)
        
        # Key is smaller than root's key
        return self.search(root.left, key)

    def inorder(self, root):
        """
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