from closest_pairs import *
from generate_pairs import *
import random

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

#
# Generate data sets of each size for use in performance metrics
# @param sizes list of sizes
# @returns set of datasets of points
#
def generate_datasets(sizes):
    datasets = []
    for size in sizes:
        dataset = generate_random_points_list(size)
        datasets.append(dataset)
    return datasets

# 
# Get the number of operations for running the brute force closest pair algorithm
# on a data set
# @param dataset to run algorithm on
def closest_pair_brute_analysis(dataset):
    n = len(dataset)
    closest_pair_brute_driver(dataset, "{0}_pairs.txt".format(n))
    analysis = get_analysis()
    operations = analysis.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))
    analysis.reset()

# 
# Get the number of operations for running the recursive closest pair algorithm
# on a data set
# @param dataset to run algorithm on
def closest_pair_recursive_analysis(dataset):
    n = len(dataset)
    closest_pair_recursive_driver(dataset, "{0}_pairs.txt".format(n))
    analysis = get_analysis()
    operations = analysis.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))
    analysis.reset()

def run_metrics_brute(datasets):
    print("Brute Force Performance:\n")
    for dataset in datasets:
        closest_pair_brute_analysis(dataset)
        clean_artifact("{0}_pairs.txt".format(len(dataset)))

def run_metrics_recursive(datasets):
    print("\nRecursive Performance:\n")
    for dataset in datasets:
        closest_pair_recursive_analysis(dataset)
        clean_artifact("{0}_pairs.txt".format(len(dataset)))

def get_default_datasets():
    sizes = [10, 29, 30, 31, 100, 1000, 5000]
    for index in range(10):
        sizes.append(random.randint(2, 1000))
    datasets = generate_datasets(sizes)
    return datasets


if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Closest Pair Performance Test", description="Run performance metrics for the closest pair algorithms")
    parser.add_argument("-n", "--size", metavar="n",  nargs="*", type=int, help="Sizes of datasets to generate")
    parser.add_argument("-b", "--brute", action="store_true", help="Run brute metrics")
    parser.add_argument("-r", "--recursive", action="store_true", help="Show algorithm analytics")
    args=parser.parse_args()
    
    if args.size:
        datasets = generate_datasets(sizes)
    else:
        datasets = get_default_datasets()

    if not args.b or args.r:
        run_metrics_brute(datasets)
        run_metrics_recursive(datasets)
 
    if args.b:
        run_metrics_brute(datasets)
    if args.r:
        run_metrics_recursive(datasets)