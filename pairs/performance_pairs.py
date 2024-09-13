from pairs import *
from generate_pairs import *
import random

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

# 
# Get the number of operations for running the brute force closest pairs algorithm
# on a data set of n random Points where 0 <= x, y <= 100
# @params n
def closest_pairs_brute_n(n):
    data_set = generate_random_points_list(n)
    result = closest_pairs_brute_driver(data_set, "{0}_pairs.txt".format(n))
    operations = result.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))

if __name__ == "__main__":
    sizes = [10, 29, 30, 31, 100, 1000, 5000]
    for index in range(10):
        sizes.append(random.randint(2, 1000))

    print("Brute Force Performance:")
    for size in sizes:
        closest_pairs_brute_n(size)
        clean_artifact("{0}_pairs.txt".format(size))