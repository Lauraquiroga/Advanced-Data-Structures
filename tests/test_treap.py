import unittest
from src.treap import Treap

class TestTreap(unittest.TestCase):
    """
    Unit test class for the `Treap` class, using Python's built-in unittest framework.
    """
    def test_insert_node(self):
        """Test if keys are inserted correctly into the treap."""
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)

        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = treap.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_insert_node_not_present(self):
        """Test that search returns False if key is not in the treap."""
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)

        # Test if a key that wasn't inserted is not found
        result, elapsed_time = treap.search_key(100)
        self.assertFalse(result)  # Should return False
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_delete_node(self):
        """Test if keys are deleted correctly from the treap."""
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)
        
        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = treap.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

        # Delete node and check the result
        treap.delete_node(30)
        self.assertFalse(treap.search_key(30)[0])  # Should return False after deletion
        self.assertTrue(treap.search_key(50)[0])   # 50 should still be present
        self.assertTrue(treap.search_key(70)[0])   # 70 should still be present

    def test_delete_node_not_present(self):
        """Test deleting a non-existent node."""
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)
        
        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = treap.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

        # Delete a non-existent node (e.g., 100)
        treap.delete_node(100)
        # Test if the keys are present
        for key in [50, 30, 70]:
            result, elapsed_time = treap.search_key(key)
            self.assertTrue(result)  # Should return True
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_empty_treap_search(self):
        """Test searching on an empty treap."""
        #Setup the Treap object for each test.
        treap = Treap()
        # Search in an empty treap
        result, elapsed_time = treap.search_key(10)
        self.assertFalse(result)  # Should return False
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_structure(self):
        """Test structure: Keeping BST property for keys and Max-Heap property for priorities"""
        #Setup the Treap object for each test.
        treap = Treap()

        small_key = 30
        large_key = 50

        # Creating a simple treap to test rotation
        treap.insert_node(large_key)
        treap.insert_node(small_key)

        # Root will depend on random priority values
        if treap.root.left:
            #       50
            #       /
            #      30
            self.assertEqual(treap.root.key, large_key) # 50 should be the root -> BST property
            self.assertGreaterEqual(treap.root.priority, treap.root.left.priority) # Max-Heap: root's priority should be >= child's priority
        else:
            #     30
            #      \
            #       50
            self.assertEqual(treap.root.key, small_key) # 30 should be the root -> BST property
            self.assertGreaterEqual(treap.root.priority, treap.root.right.priority) # Max-Heap: root's priority should be >= child's priority

        
    def test_bst_property(self):
        """Test Treap maintains the BST property"""
        treap = Treap()
        keys = [10, 20, 30, 40, 50, 25]
        for key in keys:
            treap.insert_node(key)

        def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            if not (min_val < node.key < max_val):
                return False
            return is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)

        self.assertTrue(is_bst(treap.root), "BST property violated!")