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

    def __init__(self, dataset):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (dict): A dictionary containing the full dataset to be used in benchmarking.
                        In the format:{
                        "random": [],
                        "skewed": []
                        }
   
        n_steps (int): Number of data sizes to consider in the search simulation
        """
        self.dataset = dataset
        self.data_size = len(self.dataset['random'])

        self.results_insertion = {
            "random": { "AVL": [], "RB": [], "Treap": []},
            "skewed": { "AVL": [], "RB": [], "Treap": []}
            }

        self.results_search = { "AVL": [], "RB": [], "Treap": []}
        self.sizes_search = []  # Tracking dataset sizes

        min_val = 1
        max_val = self.data_size *100
        # Generating random values to perform search simulation
        self.random_values = np.random.choice(np.arange(min_val, max_val), size=50, replace=False)

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
        print("Running Insert Simulation...")
        for distrib_key, data in self.dataset.items():
            print(distrib_key)
            structures = {"AVL": AVLTree(), "RB": RBTree(), "Treap": Treap()}
            for struc_key, tree in structures.items():
                cumulative = 0
                for i in range(len(data)):
                    _, exec_time = tree.insert_node(data[i])
                    cumulative += exec_time
                    self.results_insertion[distrib_key][struc_key].append(cumulative)
                    if i%10000==0:
                        print(i)

        Helper.save_insert_results(self.results_insertion)
    
    def simulate_search(self, n_steps=10):
        """
        Executes the benchmark by testing the BST search over each advanced data structure using increasing dataset sizes 
        (only using the random uniformly distributed dataset)

        Each search algorithm is tested on every dataset size, and their execution times are recorded.

        Parameters:
        n_steps (int): # of steps to increase the dataset size. The search is performed on each (dataset size)/n_steps

        Return:
        dict: A dictionary containing the average execution times for each algorithm across different dataset sizes.
        """
        print("Running search simulation...")
        step_size = self.data_size//n_steps
        structures = {"AVL": AVLTree(), "RB": RBTree(), "Treap": Treap()}

        for i in range(n_steps):
            length = (i+1) * step_size
            self.sizes_search.append(length)
            new_keys = self.dataset['random'][length-step_size:length]
            print(length)
            for struc_name, tree in structures.items():
                self.insert_multiple_nodes(tree, new_keys)
                self.results_search[struc_name].append(self.average_search(tree))
        
        Helper.save_search_results(self.results_search, self.sizes_search)
            

    def insert_multiple_nodes(self, tree, keys):
        for key in keys:
            tree.insert_node(key)

    def average_search(self, tree):
        """
        """
        results =[]
        for val in self.random_values:
            _, time_elapsed = tree.search_key(val)
            results.append(time_elapsed)
        return statistics.mean(results)

    def plot_insert(self, file = ''):
        """
        """
        if file:
            self.results_insertion = Helper.read_results_file(file)

        # Define dataset sizes starting from 0
        dataset_sizes = np.arange(len(next(iter(self.results_insertion['random'].values()))))

        # Plot each distribution separately all structures on same plot
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

        # Plot same structure different datasets
        for bst_type in ["AVL", "RB", "Treap"]:
            plt.figure(figsize=(6, 4))  # Create a new figure
            plt.plot(self.results_insertion["random"][bst_type], label="Random", color='red')
            plt.plot(self.results_insertion["skewed"][bst_type], label="Skewed", color='blue')
            
            plt.xlabel("Dataset Size")
            plt.ylabel("Cumulative Insertion Time (seconds)")
            plt.title(f"Cumulative Insertion Time - {bst_type}")
            plt.legend()
            plt.show()

    def plot_search(self, file = ''):
        """
        """
        if file:
            results= Helper.read_results_file(file)
            self.sizes_search = results['Data_sizes']
            self.results_search = results['Exec_times']

        plt.figure()

        plt.ylabel('Run time (s)')
        plt.xlabel('Size of the dataset')
        plt.title(f"Comparison of Run Time Complexity - BST Search")

        # Plot each algorithm's results
        for tree, times in self.results_search.items():
            plt.plot(self.sizes_search, times, label=tree, color=self.colour_key[tree])

        plt.legend()
        plt.show()

        for tree, times in self.results_search.items():
            plt.figure()

            plt.ylabel('Run time (s)')
            plt.xlabel('Size of the dataset')
            plt.title(f"Run Time Complexity - {tree}")

            plt.plot(self.sizes_search, times)

            plt.show()