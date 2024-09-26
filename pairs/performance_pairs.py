from pairs import *
from generate_pairs import *
import random

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

# 
# Get the number of operations for running the brute force closest pair algorithm
# on a data set of n random Points where 0 <= x, y <= 100
# @param n
def closest_pair_brute_n(n):
    data_set = generate_random_points_list(n)
    closest_pair_brute_driver(data_set, "{0}_pairs.txt".format(n))
    analysis = get_analysis()
    operations = analysis.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))
    analysis.reset()

# 
# Get the number of operations for running the recursive closest pair algorithm
# on a data set of n random Points where 0 <= x, y <= 100
# @param n
def closest_pair_recursive_n(n):
    data_set = generate_random_points_list(n)
    closest_pair_recursive_driver(data_set, "{0}_pairs.txt".format(n))
    analysis = get_analysis()
    operations = analysis.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))
    analysis.reset()

if __name__ == "__main__":
    # sizes = [10, 29, 30, 31, 100, 1000, 5000]
    # for index in range(10):
    #     sizes.append(random.randint(2, 1000))

    # print("Brute Force Performance:")
    # for size in sizes:
    #     closest_pair_brute_n(size)
    #     clean_artifact("{0}_pairs.txt".format(size))

    size = 50
    # print("Brute Force Performance:")
    # closest_pair_brute_n(size)
    print("Recursive Performance:")
    closest_pair_recursive_n(size)
    clean_artifact("{0}_pairs.txt".format(size))