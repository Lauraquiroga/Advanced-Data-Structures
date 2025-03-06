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

    def __init__(self, dataset, n_steps=100):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (list): A list containing the full dataset to be used in benchmarking.
        n_steps (int): Number of data sizes to consider in the search simulation
        """
        self.dataset = dataset

        self.results_insertion = {
            "Random": { "AVL": [], "RB": [], "Treap": []},
            "Skewed": { "AVL": [], "RB": [], "Treap": []},
            "Ascending": { "AVL": [], "RB": [], "Treap": []},
            "Descending": { "AVL": [], "RB": [], "Treap": []},
            }

        self.results_search = { "AVL": [], "RB": [], "Treap": []}
        self.sizes_search = []  # Tracking dataset sizes
        self.n_steps = n_steps

        self.colour_key = {
            'AVL': 'cornflowerblue',
            'RB': 'red',
            'Treap': 'green',
        }


    def simulate_insertion(self):
        pass

    def simulate_search(self):
        pass

    def plot_insert(self):
        pass

    def plot_insert_from_file(self):
        pass

    def plot_search(self):
        pass

    def plot_search_from_file(self):
        pass