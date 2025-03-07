from src.benchmark import Benchmark
from src.utils import Helper
from src.treap import Treap

def main():
    """
    Main function to load the dataset and initiate the simulation
    """
    # To generate dataset
    # size = 1000000
    # data = Helper.generate_datasets(size)
    # Helper.visualize_dataset_distribution(data)
    # Helper.save_dataset(data)

    dataset = Helper.read_json('data/dataset1M.json')
    b = Benchmark(dataset)

    #b.simulate_insertion()
    b.plot_insert_rem_outliers("insert_results_1000000_20250306-211332.json")

    #b.simulate_search(100)
    #b.plot_search("search_results_1M_steps100.json")

if __name__ == '__main__':
    main()