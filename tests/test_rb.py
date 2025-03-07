import unittest
from src.rb_tree import RBTree

class TestRBTree(unittest.TestCase):
    """
    Unit test class for the `RBTree` class, using Python's built-in unittest framework.
    """

    def test_initialization(self):
        """Test if a new tree is initialized properly."""
        rb_tree = RBTree()
        self.assertIsNone(rb_tree.root)

    def test_insert_single_node(self):
        """Test insertion of a single node."""
        rb_tree = RBTree()
        rb_tree.insert_node(10)
        self.assertIsNotNone(rb_tree.root)
        self.assertEqual(rb_tree.root.key, 10)
        self.assertEqual(rb_tree.root.color, 'B')  # Root should be black

    def test_insert_multiple_nodes(self):
        """Test insertion of multiple nodes and BST structure."""
        rb_tree = RBTree()
        keys = [10, 20, 30]
        for key in keys:
            rb_tree.insert_node(key)

        # Check if root is correct
        self.assertEqual(rb_tree.root.key, 20)  # Expecting a balanced tree
        self.assertEqual(rb_tree.root.color, 'B')  # Root must be black

        # Check if left and right children are correct
        self.assertEqual(rb_tree.root.left.key, 10)
        self.assertEqual(rb_tree.root.left.color, 'R')
        self.assertEqual(rb_tree.root.right.key, 30)
        self.assertEqual(rb_tree.root.right.color, 'R')

        # Insert 4th node and check updated structure
        rb_tree.insert_node(15)

        # Check if root is correct
        self.assertEqual(rb_tree.root.key, 20)  # Expecting a balanced tree
        self.assertEqual(rb_tree.root.color, 'B')  # Root must be black

        # Check if left and right children are correct
        self.assertEqual(rb_tree.root.left.key, 10)
        self.assertEqual(rb_tree.root.left.color, 'B')
        self.assertEqual(rb_tree.root.right.key, 30)
        self.assertEqual(rb_tree.root.right.color, 'B')
        self.assertEqual(rb_tree.root.left.right.key, 15)
        self.assertEqual(rb_tree.root.left.right.color, 'R')

    def test_search_node(self):
        """Test if keys are inserted and searched correctly within the tree."""
        #Setup the tree object for each test.
        rb_tree = RBTree()
        # Insert nodes
        rb_tree.insert_node(50)
        rb_tree.insert_node(30)
        rb_tree.insert_node(70)

        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = rb_tree.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_search_node_not_present(self):
        """Test that search returns False if key is not in the tree."""
        #Setup the tree object for each test.
        rb_tree = RBTree()
        # Insert nodes
        rb_tree.insert_node(50)
        rb_tree.insert_node(30)
        rb_tree.insert_node(70)

        # Test if a key that wasn't inserted is not found
        result, elapsed_time = rb_tree.search_key(100)
        self.assertFalse(result)  # Should return False
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_bst_property(self):
        """Test Treap maintains the BST property"""
        rb_tree = RBTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            rb_tree.insert_node(key)

        def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            if not (min_val < node.key < max_val):
                return False
            return is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)

        self.assertTrue(is_bst(rb_tree.root), "BST property violated!")

    def test_red_black_properties(self):
        """Test if the red-black properties hold after multiple insertions."""
        rb_tree = RBTree()

        keys = [10, 20, 30, 15, 25, 5, 1]
        for key in keys:
            rb_tree.insert_node(key)

        # Ensure no two consecutive red nodes exist
        def check_red_violation(node):
            if node is None:
                return True
            if node.color == 'R':
                if (node.left and node.left.color == 'R') or (node.right and node.right.color == 'R'):
                    return False
            return check_red_violation(node.left) and check_red_violation(node.right)

        self.assertTrue(check_red_violation(rb_tree.root))

        # Ensure black-height property holds
        def black_height(node):
            if node is None:
                return 1
            left_height = black_height(node.left)
            right_height = black_height(node.right)
            if left_height != right_height:
                return -1  # Indicating violation
            return left_height + (1 if node.color == 'B' else 0)

        self.assertNotEqual(black_height(rb_tree.root), -1)