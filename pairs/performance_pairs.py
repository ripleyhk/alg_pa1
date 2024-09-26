import random, argparse
from objects import Point, Pair
from main import *
from utils import *

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

# 
# Get the number of operations for running the brute force closest pair algorithm
# on a data set
# @param dataset to run algorithm on
def closest_pair_brute_analysis(dataset: list[Point]):
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
def closest_pair_recursive_analysis(dataset: list[Point]):
    n = len(dataset)
    closest_pair_recursive_driver(dataset, "{0}_pairs.txt".format(n))
    analysis = get_analysis()
    operations = analysis.operations
    print("For Data Set of size {0}, # of Operations= {1}".format(n, operations))
    analysis.reset()

def run_metrics_brute(datasets: list[list[Point]]):
    print("Brute Force Performance:")
    for dataset in datasets:
        closest_pair_brute_analysis(dataset)
        clean_artifact("{0}_pairs.txt".format(len(dataset)))

def run_metrics_recursive(datasets: list[list[Point]]):
    print("\nRecursive Performance:")
    for dataset in datasets:
        closest_pair_recursive_analysis(dataset)
        clean_artifact("{0}_pairs.txt".format(len(dataset)))

if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Closest Pair Performance Test", description="Run performance metrics for the closest pair algorithms")
    parser.add_argument("-n", "--size", metavar="n",  nargs="*", type=int, help="Sizes of datasets to generate")
    parser.add_argument("-b", "--brute", action="store_true", help="Run brute metrics")
    parser.add_argument("-r", "--recursive", action="store_true", help="Show algorithm analytics")
    args=parser.parse_args()
    
    if args.size:
        datasets = generate_datasets(args.size)
    else:
        datasets = get_default_datasets()

    if not args.brute or args.recursive:
        run_metrics_brute(datasets)
        run_metrics_recursive(datasets)
 
    if args.brute:
        run_metrics_brute(datasets)
    if args.recursive:
        run_metrics_recursive(datasets)