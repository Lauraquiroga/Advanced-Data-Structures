from datetime import datetime
import random
import string
import time
import json

class Helper:
    """
    A utility class containing helper methods for handling usernames and timing functions.
    
    The `Helper` class includes static methods to:
    - Measure the execution time of functions.
    - Load usernames from a file.
    - Create and save a new dataset of randomly generated usernames.
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
