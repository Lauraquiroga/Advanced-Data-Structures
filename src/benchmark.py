from src.treap import Treap
from src.rb_tree import RBTree
from src.avl_tree import AVLTree

from .utils import Helper

import statistics
import matplotlib.pyplot as plt
import numpy as np

class Benchmark:
    """
    Benchmarking different search algorithms by varying search space size.
    """

    def __init__(self, dataset, n_steps=100):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (dict): A dictionary containing the full dataset to be used in benchmarking.
                        In the format:{
                        "random": [],
                        "skewed": [],
                        "ascending": [],
                        "descending": []
                        }
   
        n_steps (int): Number of data sizes to consider in the search simulation
        """
        self.dataset = dataset

        self.results_insertion = {
            "random": { "AVL": [], "RB": [], "Treap": []},
            "skewed": { "AVL": [], "RB": [], "Treap": []},
            "ascending": { "AVL": [], "RB": [], "Treap": []},
            "descending": { "AVL": [], "RB": [], "Treap": []},
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
        """
        Run the insertion simulation for all the dataset distributions for all the structures

        Return:
        None
        """
        for distrib_key, data in self.dataset.items():
            structures = {"AVL": AVLTree(), "RB": RBTree(), "Treap": Treap()}
            for struc_key, tree in structures.items():
                for i in range(len(data)):
                    _, exec_time = tree.insert_node(data[i])
                    self.results_insertion[distrib_key][struc_key].append(exec_time)

        Helper.save_insert_results(self.results_insertion)

    def simulate_search(self):
        pass

    def plot_insert(self, file = ''):
        """
        """
        if file:
            self.results_insertion = Helper.read_results_file(file)

        # Define dataset sizes starting from 0
        dataset_sizes = np.arange(len(next(iter(self.results_insertion['random'].values()))))

        # Plot each distribution separately
        for dist_name, structures in self.results_insertion.items():
            plt.figure(figsize=(8, 6))
            for structure, runtimes in structures.items():
                plt.plot(dataset_sizes, runtimes, marker='o', label=structure)
            
            plt.xlabel("Dataset Size")
            plt.ylabel("Insertion Runtime (seconds)")
            plt.title(f"Insertion Complexity - {dist_name.capitalize()} Distribution")
            plt.legend()
            plt.grid()
            plt.show()

    def plot_search(self):
        pass