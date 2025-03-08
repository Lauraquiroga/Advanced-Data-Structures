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
    This class simulates insertion and search operations for different data structures (AVL, RB, and Treap).
    It collects execution times and plots the results for comparison.
    """

    def __init__(self, dataset):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (dict): A dictionary containing the full dataset to be used in benchmarking.
                        Format: {"random": [], "skewed": []}

        n_steps (int): Number of data sizes to consider in the search simulation.
        """
        self.dataset = dataset  # Dataset for benchmarking, containing random and skewed data distributions.
        self.data_size = len(self.dataset['random'])  # Size of the dataset (for random data).

        # Initialize dictionaries to store insertion results for AVL, RB, and Treap trees for both random and skewed distributions.
        self.results_insertion = {
            "random": { "AVL": [], "RB": [], "Treap": []},
            "skewed": { "AVL": [], "RB": [], "Treap": []}
        }

        # Initialize a dictionary to store search results (time) for the three tree structures.
        self.results_search = { "AVL": [], "RB": [], "Treap": []}
        self.sizes_search = []  # To track dataset sizes for search simulations.

        # Random values for search simulation across the search space.
        min_val = 1
        max_val = self.data_size * 100
        self.random_values = np.random.choice(np.arange(min_val, max_val), size=50, replace=False)

        # Dictionary mapping tree structures to specific colors for plotting.
        self.colour_key = {
            'AVL': 'cornflowerblue',
            'RB': 'red',
            'Treap': 'green',
        }

    def simulate_insertion(self):
        """
        Run the insertion simulation for all dataset distributions across all tree structures.

        This function inserts the data points into AVL, RB, and Treap trees for both random and skewed datasets,
        tracks the cumulative insertion time for each structure, and saves the results.
        """
        print("Running Insert Simulation...")
        for distrib_key, data in self.dataset.items():
            print(distrib_key)
            # Initialize tree structures.
            structures = {"AVL": AVLTree(), "RB": RBTree(), "Treap": Treap()}
            for struc_key, tree in structures.items():
                cumulative = 0
                for i in range(len(data)):
                    _, exec_time = tree.insert_node(data[i])  # Insert node and get execution time.
                    cumulative += exec_time  # Accumulate the execution time for the current insertion.
                    self.results_insertion[distrib_key][struc_key].append(cumulative)
                    if i % 10000 == 0:  # Print progress every 10,000 insertions.
                        print(i)

        Helper.save_insert_results(self.results_insertion)  # Save the insertion results.

    def simulate_search(self, n_steps=10):
        """
        Executes the benchmark by testing the BST search over each data structure using increasing dataset sizes 
        (only using the random uniformly distributed dataset).

        Parameters:
        n_steps (int): The number of steps to increase the dataset size. The search is performed on each subset
                       of the dataset by dividing it into n_steps.

        Returns:
        dict: A dictionary containing the average execution times for each algorithm across different dataset sizes.
        """
        print("Running search simulation...")
        step_size = self.data_size // n_steps  # Determine the step size for splitting the dataset.
        structures = {"AVL": AVLTree(), "RB": RBTree(), "Treap": Treap()}  # Initialize tree structures.

        for i in range(n_steps):
            length = (i + 1) * step_size  # Increase dataset size at each step.
            self.sizes_search.append(length)  # Track the size of the dataset at each step.
            new_keys = self.dataset['random'][length - step_size:length]  # Select a subset of the dataset for this step.
            print(length)
            for struc_name, tree in structures.items():
                self.insert_multiple_nodes(tree, new_keys)  # Insert nodes for the current tree.
                self.results_search[struc_name].append(self.average_search(tree))  # Record average search time for this tree.

        Helper.save_search_results(self.results_search, self.sizes_search)  # Save search results.

    def insert_multiple_nodes(self, tree, keys):
        """
        Inserts multiple nodes into a given tree.

        Parameters:
        tree: The tree structure (AVL, RB, or Treap) where nodes will be inserted.
        keys (list): A list of keys to insert into the tree.
        """
        for key in keys:
            tree.insert_node(key)  # Insert each key into the tree.

    def average_search(self, tree):
        """
        Calculates the average time taken for search operations in a tree.

        Parameters:
        tree: The tree structure to perform searches on.

        Returns:
        float: The average execution time for searching for the random values in the tree.
        """
        results = []
        for val in self.random_values:
            _, time_elapsed = tree.search_key(val)  # Perform search and get time.
            results.append(time_elapsed)  # Store the time for each search.
        return statistics.mean(results)  # Return the average of all search times.

    def plot_insert(self, file=''):
        """
        Plots the results of the insertion simulation.

        This function plots cumulative insertion times for each distribution (random and skewed) 
        and each tree structure (AVL, RB, and Treap). It also allows plotting from a saved file.

        Parameters:
        file (str): Optional file name to load saved insertion results.
        """
        if file:
            self.results_insertion = Helper.read_results_file(file)  # Load results from file if provided.

        # Define dataset sizes (x-axis) starting from 0.
        dataset_sizes = np.arange(len(next(iter(self.results_insertion['random'].values()))))

        # Plot each distribution separately for all structures on the same plot.
        for dist_name, structures in self.results_insertion.items():
            plt.figure(figsize=(8, 6))
            for structure, runtimes in structures.items():
                plt.plot(dataset_sizes, runtimes, color=self.colour_key[structure], label=structure)
            
            plt.xlabel("Dataset Size")
            plt.ylabel("Cumulative Insertion Time (seconds)")
            plt.title(f"Cumulative Insertion Time - {dist_name.capitalize()} Distribution")
            plt.legend()
            plt.grid()
            plt.show()

        Helper.check_nlogn_trend(self.results_insertion)

    def plot_search(self, file=''):
        """
        Plots the results of the search simulation.

        This function plots the execution time for each search algorithm (AVL, RB, and Treap) over increasing dataset sizes.
        It also allows plotting from a saved file.

        Parameters:
        file (str): Optional file name to load saved search results.
        """
        if file:
            results = Helper.read_results_file(file)
            self.sizes_search = results['Data_sizes']  # Load dataset sizes.
            self.results_search = results['Exec_times']  # Load execution times.

        plt.figure()
        plt.ylabel('Run time (s)')
        plt.xlabel('Size of the dataset')
        plt.title(f"Comparison of Run Time Complexity - BST Search")

        # Plot each algorithm's results.
        for tree, times in self.results_search.items():
            plt.plot(self.sizes_search, times, label=tree, color=self.colour_key[tree])

        plt.legend()
        plt.show()

        results = {
            "Exec_times": self.results_search,
            "Data_sizes": self.sizes_search
        }
        Helper.check_log_trend(results)