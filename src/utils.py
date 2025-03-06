import numpy as np
from datetime import datetime
import time
import json

class Helper:
    """
    A utility class containing helper methods for handling usernames and timing functions.
    
    The `Helper` class includes static methods to:
    - Measure the execution time of functions.
    - Load data from a file.
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
        pass

    @staticmethod
    def generate_datasets(dataset_size, max_val=10000):
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
        list of 
        """
        random = np.random.uniform(1, max_val, dataset_size).astype(int)
        mean=5000
        std_dev=1000
        skewed = np.random.normal(mean, std_dev, dataset_size).astype(int)
        ascending = np.arange(1, 1 + dataset_size)
        descending =  np.arange(dataset_size, 0, -1)
        return {'random':random, 'skewed': skewed, 'ascending':ascending, 'descending':descending}

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
            filename = f"data/results/benchmark_results_{final_size}_steps{num_steps}_{timestamp}.json"

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
    def read_search_results_json(filename):
        """
        Read the JSON file and store its content in 'results'.
        The structure of the json file is as follows:
        {
            "Exec_times": { "AVL": [], "RB": [], "Treap": []},
            "Data_sizes": []
        }

        Return:
        (dict): the variable storing the data from the json file
        """
        # 
        with open(filename, 'r') as file:
            results = json.load(file)

        return results