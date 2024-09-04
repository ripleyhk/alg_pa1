'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Problem 1: Closest Pairs
# Description: A suite of algorithms for pairing Points (x, y), based on proximity
'''

# ---------- Display Functions ----------
'''
# The following functions are used to display the results of the pairing algorithm,
# either to the console/terminal, for result pair lists <= 30
# or to an output file (pairs.txt by default)
#
# This functionality is not being evaluated for running time complexity
'''

# Display pairs, either by printing to console (pairs list length <= 30)
# or by writing to a file (either user-specified or pairs.txt by default)
def display_pairs(pairs, filename='pairs.txt'):
    if (len(pairs) <= 30):
        print_pairs(pairs)
    else:
        write_pairs(pairs, filename)

# Print pairs to console
# @param pairs list of pairs of closest points
def print_pairs(pairs):
    for pair in pairs:
        print(pair)

# Write pairs to file, (pairs)
# @param pairs list of pairs of closest points
# @param filename name of file to write pairs list to
def write_pairs(pairs, filename):
    f = open(filename, "w")
    for pair in pairs:
        f.write("{0}\n".format(pair))
    f.close()

# ---------- Object Functions ----------
'''
# The following structure is used to represent a Point with x and y coordinates
#
# This functionality is not being evaluated for running time complexity
'''
class Point:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "[{0},{1}]".format(self.x, self.y)

    def __repr__(self):
        return "[{0},{1}]".format(self.x, self.y)
    
# ---------- Algorithm Functions ----------
