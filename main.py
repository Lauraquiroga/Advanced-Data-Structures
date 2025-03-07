from src.benchmark import Benchmark
from src.utils import Helper

def generate_dataset(size = 1000000):
    """
    Generates a dataset of the specified size, visualizes its distribution, and saves it to a file.

    Parameters:
    size (int): The number of elements in the dataset (default is 1,000,000).

    Returns:
    dict: A dictionary containing the generated dataset with keys like 'random', 'skewed', etc.
    """
    # Generate the dataset using Helper's method
    data = Helper.generate_datasets(size)
    
    # Visualize the distribution of the dataset
    Helper.visualize_dataset_distribution(data)
    
    # Save the generated dataset to a file
    Helper.save_dataset(data)
    
    return data

def simulate_insertion(b):
    """
    Simulates the insertion process for the Benchmark instance and plots the results.

    Parameters:
    b (Benchmark): The Benchmark object on which the insertion simulation is to be run.
    
    Returns:
    None
    """
    # Run the insertion simulation and plot the insertion times
    b.simulate_insertion()
    b.plot_insert()

def simulate_search(b, steps=100):
    """
    Simulates the search process for the Benchmark instance and plots the results.

    Parameters:
    b (Benchmark): The Benchmark object on which the search simulation is to be run.
    steps (int): The number of steps to divide the dataset size for search simulation (default is 100).
    
    Returns:
    None
    """
    # Run the search simulation and plot the search times
    b.simulate_search(steps)
    b.plot_search()

def main():
    """
    Main function to load the dataset, initialize the benchmarking process, and run the simulations.
    
    - Loads the dataset from a JSON file.
    - Runs both insertion and search simulations.
    
    Returns:
    None
    """
    # Read the dataset from a JSON file (can be modified to use a different file)
    dataset = Helper.read_json('data/dataset10.json')  # Change file name to test with another dataset
    
    # Initialize the Benchmark object with the loaded dataset
    b = Benchmark(dataset)
    
    # Run the insertion simulation and plot the results
    #simulate_insertion(b)
    
    # Run the search simulation and plot the results (with 10 steps in this case)
    #simulate_search(b, 10)

    # Uncomment below lines if you want to plot the results from pre-saved files
    b.plot_search("search_results_1M_steps100.json")  # Sample plot search from file
    # b.plot_insert('insert_results_1M_cumulative.json')  # Sample plot insert from file

if __name__ == '__main__':
    # Start the main program execution
    main()