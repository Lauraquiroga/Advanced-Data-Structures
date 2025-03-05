from src.treap import Treap
from src.rb_tree import RBTree
from src.avl_tree import AVLTree

def main():
    """
    Main function to load the dataset and initiate the login check simulation.

    This function loads the usernames from a file and passes them to the LoginChecker 
    to perform the benchmark simulation.
    """
    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        tree.insert_node(key)
    tree.show()

    avl_tree = AVLTree()
    keys = [10, 20, 30]
    for key in keys:
        avl_tree.insert_node(key)
    avl_tree.show()

if __name__ == '__main__':
    main()