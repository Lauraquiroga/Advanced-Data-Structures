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
        """
        Test if keys are inserted and searched correctly within the tree.
        """
        #Setup the Treap object for each test.
        rb_tree = RBTree()
        # Insert nodes
        rb_tree.insert_node(50)
        rb_tree.insert_node(30)
        rb_tree.insert_node(70)

        # Test if the keys are present
        self.assertTrue(rb_tree.search_key(50))  # Should return True
        self.assertTrue(rb_tree.search_key(30))  # Should return True
        self.assertTrue(rb_tree.search_key(70))  # Should return True

    def test_search_node_not_present(self):
        """
        Test that search returns False if key is not in the tree.
        """
        #Setup the Treap object for each test.
        rb_tree = RBTree()
        # Insert nodes
        rb_tree.insert_node(50)
        rb_tree.insert_node(30)
        rb_tree.insert_node(70)

        # Test if a key that wasn't inserted is not found
        self.assertFalse(rb_tree.search_key(100))  # Should return False