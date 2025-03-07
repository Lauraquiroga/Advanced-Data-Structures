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

    dataset = Helper.read_json('data/dataset10.json')
    b = Benchmark(dataset)
    #b.simulate_insertion()
    #b.plot_insert_log("insert_results_1M.json")
    b.simulate_search()
    b.plot_search()


    # treap = Treap()
    # treap.insert_node(90)
    # treap.insert_node(10)
    # treap.show()

if __name__ == '__main__':
    main()