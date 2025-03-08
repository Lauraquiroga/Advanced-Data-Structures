import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from sklearn.metrics import r2_score
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
        {'random':[], 'skewed': []}
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
        {'random':[], 'skewed': []}
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
    
    @staticmethod
    def check_log_trend(search_results):
        """
        Check if the search results exhibit a logarithmic trend for each of the structures.
        Plots them individually with their logarithmic fit.

        Parameters:
        search_results (dict): A dictionary containing the results of the search simulation in the format:
        {
            "Exec_times": { "AVL": [], "RB": [], "Treap": []},
            "Data_sizes": []
        }
        """
        def log_func(x, a, b):
            return a + b * np.log(x)
        
        for struc_key, struc_times in search_results["Exec_times"].items():

            x = np.array(search_results["Data_sizes"])
            y = np.array(struc_times)
            # Perform curve fitting
            params, covariance = curve_fit(log_func, x, y)
            a, b = params  # Extract fitted parameters

            # Compute fitted values
            y_fit = log_func(x, a, b)

            # Plot the original data and the logarithmic fit
            plt.scatter(x, y, label="Original Data", color='blue')
            plt.plot(x, y_fit, 'r--', label=f"Logarithmic Fit: y = {a:.7f} + {b:.7f} log(x)", linewidth=2)
            plt.xlabel("Input Size")
            plt.ylabel("Runtime")
            plt.title(f"Logarithmic Fit Analysis - BST Search ({struc_key})")
            plt.legend()
            plt.grid()
            plt.show()

            # Print the fitted parameters
            print(f"{struc_key} - Fitted Parameters: a = {a}, b = {b}")
            # Check goodness of fit (r^2 value)
            r2 = r2_score(y, y_fit)
            print(f"R²: {r2}")

    @staticmethod
    def check_nlogn_trend(insertion_results):
        """
        Check if the search results exhibit a n log n trend for each of the structures.
        Plots them individually with their n log n fit.

        Parameters:
        search_results (dict): A dictionary containing the results of the search simulation in the format:
        {
        "random": { "AVL": [], "RB": [], "Treap": []},
        "skewed": { "AVL": [], "RB": [], "Treap": []}
        }
        """

        # Define dataset sizes (x-axis) starting from 0.
        dataset_sizes = np.arange(len(next(iter(insertion_results['random'].values()))))
        
        for distrib_key, exect_dict in insertion_results.items():
            for struc_key, struc_times in exect_dict.items():

                x = np.array(dataset_sizes[1:]) #skippping 0 point
                y = np.array(struc_times[1:])#skippping 0 point
                # Perform curve fitting
                n_log_n = x * np.log(x)
                slope, intercept, r_value, p_value, std_err = stats.linregress(n_log_n, y)

                if distrib_key == 'random':
                    distrib = "Random Uniform"
                else:
                    distrib = "Random Skewed"

                # Plotting the data
                plt.title(f"{distrib}: n log n Fit Analysis - Cumulative Insert({struc_key})")
                plt.plot(x, y, label='Original Data')
                plt.plot(x, slope * n_log_n + intercept, color='red', label=f'Fit: y = {slope:.2e} * n log(n) + {intercept:.2e}')
                plt.xlabel('Dataset Size')
                plt.ylabel('Cumulative Insertion Time (s)')
                plt.legend()
                plt.show()

                print(f"{distrib_key} {struc_key} - Fitted parameters: slope={slope}, intercept={intercept}")
                # Output the R-squared value to assess the fit quality
                print(f"R-squared value: {r_value**2}")