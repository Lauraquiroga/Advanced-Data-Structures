# Advanced Data Structures     
Advanced Algorithms (COSC 520) - Assignment 2      
Author: Laura Quiroga (lquiroga)     

This project implements three comparable advanced data structures: AVL tree, Red-Black tree, and Treap. It also includes a numerical comparison of their performance in terms of time complexity for the search and insert operations.

## Project Structure
📂 project_root/     
│── 📂 assets/  <-- Folder where the plots showing the run time complexities of the 3 structures are stored        
│&emsp;&emsp;│── COSC 520 -Assignment 2.pdf  <-- The assignment instructions      
│      
│── 📂 data/     
│&emsp;&emsp;│── dataset1M.txt  <-- Dataset file used to perform the runtime complexity analysis (synthetic data)    
│&emsp;&emsp;│── dataset10.txt  <-- Dataset dummy file used to show format and perform tests (synthetic data)   
│&emsp;&emsp;│── 📂 results/  <-- Folder where results are stored after executing the program           
│        
│── 📂 src/   
│&emsp;&emsp;│── benchmark.py   <-- Script to benchmark the data structures       
│&emsp;&emsp;│── utils.py       <-- Utility functions (e.g., generate_datasets)     
│&emsp;&emsp;│── base_tree.py  <-- Defines an abstract base class for BST tree structure     
│&emsp;&emsp;│── avl_tree.py  <-- Implementation of AVL tree       
│&emsp;&emsp;│── rb_tree.py  <-- Implementation of Red-Black tree    
│&emsp;&emsp;│── treap.py  <-- Implementation of Treap  
│&emsp;&emsp;│── avl_node.py  <-- Implementation of AVL tree node    
│&emsp;&emsp;│── rb_node.py  <-- Implementation of Red-Black tree node    
│&emsp;&emsp;│── treap_node.py  <-- Implementation of Treap Node       
│       
│── 📂 tests/  <-- Unit tests     
│&emsp;&emsp;│── test_avl.py  <-- Unit tests for the AVL tree    
│&emsp;&emsp;│── test_rb.py  <-- Unit tests for the Red-Black tree     
│&emsp;&emsp;│── test_treap.py  <-- Unit tests for the Treap    
│      
│── README.md       
│── main.py  <-- File containing main Python script             
│── requirements.txt  <-- Project requirements           

## Setup instructions   
Follow these steps to run the project:
1. **Clone the project**
   ```bash
   git clone https://github.com/Lauraquiroga/Advanced-Data-Structures.git
   cd Advanced-Data-Structures
   ```
2.  **Install dependencies**           
   Ensure that you have Python installed on your system.     
   Create and activate a virtual environment (recommended version for the virtual environment: Python 3.12.7).       

   Install requirements mentioned in the requirements.txt file.       
   
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the project**       
   Run the project from the root folder.       
   ```bash
   python main.py # or use python3 main.py if needed
   ```
   This will run the simulation with the small dataset included in the data folder (dataset10.json).          

   After the execution, the results will be saved in the data/results folder and you will see the plots showing the run time complexities.
           
   To use the 1M dataset or a custom one, place your file in the data folder and update the filename in main.py in the main() function.
                
   If you want to run the project with a different number of simulation steps (variations of sizes in the dataset), update the n_steps parameter in the initialization of the Benchmark() object in the main.py file.     
           

5. **Run the unit tests**            
   To run the test cases use the following command.       
   ```bash
   python -m unittest discover -s tests # or use python3 -m unittest discover -s tests if needed
   ```
   
## References
Code in the AVLTree and AVLNode classes was adapted from:       
GeeksforGeeks. Insertion in an AVL Tree. Accessed: 2025-03-07. 2025. url: https://www.geeksforgeeks.org/insertion-in-an-avl-tree/.         

Code in the RBTree and RBNode classes was adapted from:       
 GeeksforGeeks. Insertion in Red-Black Tree. Accessed: 2025-03-07. 2025. url: https://www.geeksforgeeks.org/insertion-in-red-black-tree/.       

Code in the Treap and TreapNode classes was adapted from:      
GeeksforGeeks. Implementation of Search, Insert and Delete in Treap. Accessed: 2025-03-07.
2025. url: https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/.
