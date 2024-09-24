from turing import *
import random

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for evaluating performance of Closest Pairs implementations
'''

#
# Generate a random unary subtraction tape for two operands
# totaling in a length of n
#
def generate_subtraction_n(n):
    tape = ""
    midpoint = random.randint(1, n-1)
    for i in range(midpoint):
        tape+= "1"
    tape += "#"
    for i in range(midpoint+1, n):
        tape+= "1"
    return tape

# 
# Get the number of operations for running the turing algorithm
# @params n
def turing_n(n):
    input = generate_subtraction_n(n)
    turing_driver(input)
    analyis = get_analysis()
    operations = analysis.operations
    space = analysis.space
    print("For Data Set of size {0}, # of Operations= {1}, # of Cells= {2}".format(n, operations, space))
    analyis.reset()

if __name__ == "__main__":
    sizes = [10, 29, 30, 31, 100, 1000, 5000]
    for index in range(10):
        sizes.append(random.randint(2, 1000))

    print("DTM Performance:")
    for size in sizes:
        turing_n(size)