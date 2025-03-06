from src.benchmark import Benchmark
from src.utils import Helper
from src.avl_tree import AVLTree

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
    b.simulate_insertion()


if __name__ == '__main__':
    main()