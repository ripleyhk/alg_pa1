from turing import *
import random

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

#
# Generate a random unary subtraction tape for two operands
# @param n total length of input, including both operands and dividing '#'
# @returns a valid input string for unary subtraction
#
def generate_subtraction_n(n) -> str:
    tape = ""
    midpoint = random.randint(1, n-1)
    for i in range(midpoint):
        tape+= "1"
    tape += "#"
    for i in range(midpoint+1, n):
        tape+= "1"
    return tape

#
# Generate data sets of each size for use in performance metrics
# @param sizes list of sizes
# @returns set of datasets of unary subtraction strings
#
def generate_datasets(sizes) -> list[str]:
    datasets = []
    for size in sizes:
        dataset = generate_subtraction_n(size)
        datasets.append(dataset)
    return datasets

# 
# Get the number of operations for running the turing algorithm
# @params input string comprising a unary subtraction
def turing_analysis(input):
    n = len(input)
    result = turing_driver(input)
    analyis = get_analysis()
    operations = analysis.operations
    space = analysis.space
    print("For Data Set of size {0}, # of Operations= {1}, # of Cells= {2}".format(n, operations, space))
    analyis.reset()

# Run analytics using the default dataset sizes
def run_default_metrics():
    sizes = [10, 29, 30, 31, 100, 1000, 5000]
    for index in range(10):
        sizes.append(random.randint(2, 1000))
    datasets = generate_datasets(sizes)
    for input in datasets:
        turing_analysis(input)

if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="DTM Performance Test", description="Run performance metrics for DTM unary subtraction")
    parser.add_argument("-n", "--sizes", metavar="n", nargs="*", type=int, help="Sizes of datasets to generate")
    args=parser.parse_args()
    
    print("DTM Performance:")
    sizes = args.sizes
    if not args.sizes:
        run_default_metrics()
    else:
        datasets = generate_datasets(sizes)
        for input in datasets:
            turing_analysis(input)