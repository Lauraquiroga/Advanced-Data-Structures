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

        # Check if root is correct
        self.assertEqual(avl_tree.root.key, 20)
        self.assertEqual(avl_tree.root.height, 2)

        # Check if left and right children are correct
        self.assertEqual(avl_tree.root.left.key, 10)
        self.assertEqual(avl_tree.root.left.height, 1)
        self.assertEqual(avl_tree.root.right.key, 30)
        self.assertEqual(avl_tree.root.left.height, 1)

        # Insert 4,5,6-th nodes and check updated structure
        new_keys = [40, 50, 25]
        for key in new_keys:
            avl_tree.insert_node(key)

        # Check if root is correct
        self.assertEqual(avl_tree.root.key, 30)
        self.assertEqual(avl_tree.root.height, 3)

    def test_search_node(self):
        """Test if keys are inserted and searched correctly within the tree."""
        #Setup the tree object for each test.
        avl_tree = AVLTree()
        # Insert nodes
        avl_tree.insert_node(50)
        avl_tree.insert_node(30)
        avl_tree.insert_node(70)

        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = avl_tree.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_search_node_not_present(self):
        """Test that search returns False if key is not in the tree."""
        #Setup the tree object for each test.
        avl_tree = AVLTree()
        # Insert nodes
        avl_tree.insert_node(50)
        avl_tree.insert_node(30)
        avl_tree.insert_node(70)

        # Test if a key that wasn't inserted is not found
        result, elapsed_time = avl_tree.search_key(100)
        self.assertFalse(result)  # Should return False
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_insert_balanced(self):
        """Test insertion maintains AVL tree balance"""
        avl_tree = AVLTree()
        keys = [10, 20, 30, 40, 50, 25]  # Known unbalanced sequence
        for key in keys:
            avl_tree.insert_node(key)

        # Verify AVL property: balance factor must be -1, 0, or 1
        def check_balance(node):
            if not node:
                return True
            balance = avl_tree.get_balance(node)
            self.assertIn(balance, [-1, 0, 1], f"Unbalanced node {node.key} with balance {balance}")
            return check_balance(node.left) and check_balance(node.right)

        self.assertTrue(check_balance(avl_tree.root))

    def test_bst_property(self):
        """Test AVL tree maintains the BST property"""
        avl_tree = AVLTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            avl_tree.insert_node(key)

        def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            if not (min_val < node.key < max_val):
                return False
            return is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)

        self.assertTrue(is_bst(avl_tree.root), "BST property violated!")

    def test_height_property(self):
        """Test if height is correctly updated after insertions"""
        avl_tree = AVLTree()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            avl_tree.insert_node(key)

        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            expected_height = 1 + max(left_height, right_height)
            self.assertEqual(node.height, expected_height, f"Height error at node {node.key}")
            return expected_height

        check_height(avl_tree.root)