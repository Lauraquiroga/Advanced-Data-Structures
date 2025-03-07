from src.benchmark import Benchmark
from src.utils import Helper

def generate_dataset(size = 1000000):
    # To generate dataset
    data = Helper.generate_datasets(size)
    Helper.visualize_dataset_distribution(data)
    Helper.save_dataset(data)
    return data

def simulate_insertion(b):
    b.simulate_insertion()
    b.plot_insert()

def simulate_search(b, steps=100):
    b.simulate_search(steps)
    b.plot_search()

def main():
    """
    Main function to load the dataset and initiate the simulation
    """
    dataset = Helper.read_json('data/dataset10.json') # Change file name to test with another dataset
    b = Benchmark(dataset)
    simulate_insertion(b)
    simulate_search(b, 10)

    #b.plot_search("search_results_1M_steps100.json") # Sample plot search from file
    #b.plot_insert('insert_results_1M_cumulative.json') # Sample plot insert from file

if __name__ == '__main__':
    main()