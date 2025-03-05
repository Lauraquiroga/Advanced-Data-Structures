from src.treap import Treap
from src.rb_tree import RBTree

def main():
    """
    Main function to load the dataset and initiate the login check simulation.

    This function loads the usernames from a file and passes them to the LoginChecker 
    to perform the benchmark simulation.
    """
    rb_tree = RBTree()
    keys = [10, 20, 30, 15]
    for key in keys:
        rb_tree.insert_node(key)
    rb_tree.show_rbtree()

if __name__ == '__main__':
    main()