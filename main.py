from src.treap import Treap

def main():
    """
    Main function to load the dataset and initiate the login check simulation.

    This function loads the usernames from a file and passes them to the LoginChecker 
    to perform the benchmark simulation.
    """
    treap = Treap()
    treap.show_treap()
    treap.insert_node("aa")
    treap.insert_node("ab")
    treap.insert_node("bb")
    treap.delete_node("aa")
    treap.search_key("ab")
    treap.show_treap()

if __name__ == '__main__':
    main()