from src.treap import Treap
from src.rb_tree import RBTree
from src.avl_tree import AVLTree

from .utils import Helper

import statistics
import matplotlib.pyplot as plt

class Benchmark:
    """
    Benchmarking different search algorithms by varying search space size.
    """

    def __init__(self, dataset, n_steps=10):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (list): A list containing the full dataset to be used in benchmarking.
        n_steps (int): Number of data sizes to consider in the simulation
        """
        self.dataset = dataset