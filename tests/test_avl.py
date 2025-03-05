import unittest
from src.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    """
    Unit test class for the `AVLTree` class, using Python's built-in unittest framework.
    """

    def test_initialization(self):
        """Test if a new tree is initialized properly."""
        avl_tree = AVLTree()
        self.assertIsNone(avl_tree.root)

    def test_insert_single_node(self):
        """Test insertion of a single node."""
        avl_tree = AVLTree()
        avl_tree.insert_node(10)
        self.assertIsNotNone(avl_tree.root)
        self.assertEqual(avl_tree.root.key, 10)
        self.assertEqual(avl_tree.root.height, 1) #Height should be 1

    def test_insert_multiple_nodes(self):
        """Test insertion of multiple nodes and BST structure."""
        avl_tree = AVLTree()
        keys = [10, 20, 30]
        for key in keys:
            avl_tree.insert_node(key)

        self.assertEqual(avl_tree.root.key, 20)
        self.assertEqual(avl_tree.root.height, 2)

        # Check if left and right children are correct
        self.assertEqual(avl_tree.root.left.key, 10)
        self.assertEqual(avl_tree.root.right.key, 30)