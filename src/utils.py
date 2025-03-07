import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import json
import os

class Helper:
    """
    A utility class containing helper methods for handling results, dataset generation, and timing functions.
    
    The `Helper` class includes static methods to:
    - Measure the execution time of functions.
    - Generate a dataset
    - Load data from a file.
    - Save data into a file
    - Visualize dataset distribution
    """

    @staticmethod
    def timing_decorator(func):
        """
        A decorator that measures the execution time of a function.
        
        This decorator wraps around a function, calculates the time taken to execute the function,
        and returns both the result of the function and the elapsed time.

        Parameters:
        func (function): The function to be wrapped and timed.

        Returns:
        tuple: A tuple containing the result of the function and the execution time in seconds.
        """
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            return result, elapsed_time  # Return both the function result and execution time
        return wrapper

    @staticmethod
    def save_dataset(dataset):
        """
        Save dataset into a json file with a timestamp suffix in the filename.

        Parameters:
        dataset (dict): A dictionary in the format:
        {'random':[], 'skewed': [], 'ascending':[], 'descending':[]}
        containing the dataset to be saved.

        File format:
        The file will be saved in the './data/' directory with a filename that includes a timestamp
        (format: YYYYMMDD_HHMMSS).
        """
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"data/dataset1M_{timestamp}.json"

            with open(filename, "w") as file:
                json.dump(dataset, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving dataset: {e}")
            return False

    @staticmethod
    def generate_datasets(dataset_size):
        """
        Generate the datasets:
        - 1M Asciending order
        - 1M Desceding order
        - 1M Random uniform
        - 1M Random skewed

        Parameters:
        dataset_size (int): The size of the dataset
        max_val (int): maximum value in the range

        Returns:
        dict: The generated dataset in the format:
        {
        'random': random.tolist(),
        'skewed': skewed.tolist()
        }
        """
        min_val = 1
        max_val = dataset_size*100

        # Generating random uniform array
        random = np.random.choice(np.arange(min_val, max_val), size=dataset_size, replace=False)

        # Generating random skewed array
        skew_factor=2.0
        pool = np.arange(min_val, max_val + 1)
        probabilities = np.exp(-skew_factor * (pool - min_val) / (max_val - min_val))
        probabilities /= probabilities.sum()
        skewed = np.random.choice(pool, size=dataset_size, replace=False, p=probabilities)

        # Create the dataset dictionary -> from np arrays to lists so that they can be saved into a json file
        datasets = {
        'random': random.tolist(),
        'skewed': skewed.tolist()
        }
        return datasets
    
    def visualize_dataset_distribution(dataset):
        """
        Creates a histogram visualization for the dataset
        
        Parameters:
        dataset (dict): A dictionary containing the dataset in the format:
        {'random':[], 'skewed': [], 'ascending':[], 'descending':[]}
        """
        for key, array in dataset.items():
            plt.figure(figsize=(10, 6))
            sns.histplot(array, kde=True, bins=30, color='blue')
            plt.title(f'Histogram of {key} data')
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.show()

    @staticmethod
    def save_search_results(exec_times, data_sizes):
        """
        Saves the results of the simulation into a JSON file with a unique filename.

        The filename is generated dynamically using:
        - The final dataset size analyzed
        - The number of steps in between data sizes
        - A timestamp for uniqueness

        Format:
        {
            "Exec_times": { "AVL": [], "RB": [], "Treap": []},
            "Data_sizes": []
        }

        Parameters:
        exec_times (dict): The results of the simulation, in the format:
                        { "AVL": [], "RB": [], "Treap": []}
        data_sizes (list of int): The dataset sizes that correspond to the execution times.

        Returns:
        bool: True if the file is saved successfully, False otherwise.
        """
        try:
            final_size = data_sizes[-1] if data_sizes else "unknown"
            num_steps = len(data_sizes)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"data/results/search_results_{final_size}_steps{num_steps}_{timestamp}.json"

            results = {
            "Exec_times": exec_times,
            "Data_sizes": data_sizes
            }

            with open(filename, "w") as file:
                json.dump(results, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False
        
    @staticmethod
    def save_insert_results(results):
        """
        Saves the results of the simulation into a JSON file with a unique filename.

        The filename is generated dynamically using:
        - The final dataset size analyzed
        - The number of steps in between data sizes
        - A timestamp for uniqueness

        The json file will follow the same format as the results parameter's

        Parameters:
        results (dict): The results of the insertion simulation in the format:
        {
        "random": { "AVL": [], "RB": [], "Treap": []},
        "skewed": { "AVL": [], "RB": [], "Treap": []}
        }

        Returns:
        bool: True if the file is saved successfully, False otherwise.
        """
        try:
            final_size = len(results['random']['AVL'])
            timestamp = time.strftime("%Y%m%d-%H%M%S")

            sibling_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
            os.makedirs(sibling_folder, exist_ok=True)
            file_path = os.path.join(sibling_folder, f"results/insert_results_{final_size}_{timestamp}.json")

            with open(file_path, "w") as file:
                json.dump(results, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False

    @staticmethod
    def read_results_file(filename):
        """
        Read the given JSON file from the results folder and return its contents

        Parameters:
        filename (str): the name of the json file to read

        Return:
        (dict): the variable storing the data from the json file
        """
        sibling_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
        os.makedirs(sibling_folder, exist_ok=True)
        file_path = os.path.join(sibling_folder, f"results/{filename}")
        with open(file_path, 'r') as file:
            content = json.load(file)

        return content

    @staticmethod
    def read_json(filename):
        """
        Read the given JSON file and return its contents

        Parameters:
        filename (str): the name of the json file to read

        Return:
        (dict): the variable storing the data from the json file
        """
        with open(filename, 'r') as file:
            content = json.load(file)

        return content