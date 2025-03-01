import unittest
import random
from src.treap import Treap

class TestTreap(unittest.TestCase):
    """
    Unit test class for the `Treap` class, using Python's built-in unittest framework.
    """
    def test_insert_node(self):
        """
        Test if keys are inserted correctly into the treap.
        """
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)

        # Test if the keys are present
        self.assertTrue(treap.search_key(50))  # Should return True
        self.assertTrue(treap.search_key(30))  # Should return True
        self.assertTrue(treap.search_key(70))  # Should return True

    def test_insert_node_not_present(self):
        """
        Test that search returns False if key is not in the treap.
        """
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)

        # Test if a key that wasn't inserted is not found
        self.assertFalse(treap.search_key(100))  # Should return False

    def test_delete_node(self):
        """
        Test if keys are deleted correctly from the treap.
        """
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)
        
        # Check that the nodes are inserted
        self.assertTrue(treap.search_key(50))
        self.assertTrue(treap.search_key(30))
        self.assertTrue(treap.search_key(70))

        # Delete node and check the result
        treap.delete_node(30)
        self.assertFalse(treap.search_key(30))  # Should return False after deletion
        self.assertTrue(treap.search_key(50))   # 50 should still be present
        self.assertTrue(treap.search_key(70))   # 70 should still be present

    def test_delete_node_not_present(self):
        """
        Test deleting a non-existent node.
        """
        #Setup the Treap object for each test.
        treap = Treap()
        # Insert nodes
        treap.insert_node(50)
        treap.insert_node(30)
        treap.insert_node(70)
        
        # Check that the nodes are inserted
        self.assertTrue(treap.search_key(50))
        self.assertTrue(treap.search_key(30))
        self.assertTrue(treap.search_key(70))

        # Delete a non-existent node (e.g., 100)
        treap.delete_node(100)
        self.assertTrue(treap.search_key(50))   # 50 should still be present
        self.assertTrue(treap.search_key(30))   # 30 should still be present
        self.assertTrue(treap.search_key(70))   # 70 should still be present

    def test_empty_treap_search(self):
        """
        Test searching on an empty treap.
        """
        #Setup the Treap object for each test.
        treap = Treap()
        # Search in an empty treap
        self.assertFalse(treap.search_key(10))  # Should return False

    def test_structure(self):
        """
        Test structure: Keeping BST property for keys and Max-Heap property for priorities
        """
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