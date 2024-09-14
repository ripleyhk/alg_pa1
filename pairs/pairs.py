import math

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
# @param pairs list of pairs of closest points
# @param filename name of file to write pairs list to
# or by writing to a file (either user-specified or pairs.txt by default)
def display_pairs(pairs, filename):
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

    def __eq__(self, other):
        return (math.isclose(self.x, other.x)) and (math.isclose(self.y, other.y))
    
'''
# The following structure is used to represent a Pair of points and their distance
#
# This functionality is not being evaluated for running time complexity
'''
class Pair:
    def __init__ (self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

    def get_pair(self):
        return (self.point1, self.point2)

    def __str__(self):
        return "({0}, {1})".format(self.point1, self.point2)

    def __repr__(self):
        return "({0}, {1})".format(self.point1, self.point2)

    def __eq__(self, other):
        if type(other) is Pair:
            return self.get_pair() == other.get_pair()
        return self.get_pair() == other
'''
# The following structure is used to hold both the result and operation count for a particular
# execution of a function, for use in complexity analysis
#
# This functionality is not being evaluated for running time complexity
'''
class Analysis:
    def __init__ (self, result, operations):
        self.result = result
        self.operations = operations

    def __str__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)

    def __repr__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)
        
    
# ---------- Utility Functions ----------
'''
# The following functions are used to determine the distance between two Points
# It is used by the algorithm implementions for both Problems 1.b and 1.d
#
# Calculating the distance between two Points should conceptually be understood to be
# a single discrete operation of running time O(1)
#
'''

# Calculate the Euclidian distance sqrt((x2-x1)^2+(y2-y1)^2)
# @param point1 first point, containing an x and y coordinate
# @param point 2 second point, containing an x and y coordinate
# @returns Euclidian distance between point1 and point2
def calculate_distance(point1, point2):
    delta_x2 = math.pow(point2.x - point1.x, 2)
    delta_y2 = math.pow(point2.y - point1.y, 2)
    distance = math.sqrt(delta_x2 + delta_y2)
    return distance


# ---------- Brute Force Method (1.a-b) ----------
'''
# Pseudocode (1.a):
#
# List of Pairs = EMPTY LIST
# For index1 starting at 0 -> length of Data Set A:
#   initial minimum distance = INFINITY (so any actual distance will be smaller)
#   index of closest Point = UNDEFINED (because no comparisons have been made yet)
#   For index2 starting at 0 -> length of Data Set A:
#       skip over index1 == index2 (because the Point should not consider itself as a closet Point)
#       distance = euclidian distance(Point at index1, Point at index2)
#       if distance is smaller than the current mimimum distance:
#           update minimum distance = distance
#           update index of closest Point = index2
#   Create a new Pair containing the Point at index1 and the Point at the index of the closest Point
#   Add new Pair to the List of Pairs
#   Write Results to Either Console or File
'''

'''
# Brute Force Implementation (1.b)
# Description: Find the closest Point to each Point in the Data Set
# Either print the results to console if the size of the data set <= 30
# Else write the results to pairs.txt
'''

# 
# Main function for calculating the closest pairs using the brute force algorithm described above
# @params points Data Set containing a list of Points
# @returns an Analysis object, containing both the list of pairs generated by the brute force algorithm
# as well as a count of the number of distance calculations, for use in complexity analysis
def closest_pairs_brute(points):
    pairs = []
    operations = 0
    for index_i in range(len(points)):
        min_distance = math.inf
        closest_index = -1
        for index_j in range(len(points)):
            if (index_i == index_j): 
                continue
            '''
            # In order to evaluate the complexity of this algorithm, we will be
            # counting the number of times the distance must be calculated between
            # any two Points
            '''
            distance = calculate_distance(points[index_i], points[index_j])
            operations += 1
            if (distance < min_distance):
                min_distance = distance
                closest_index = index_j
        pair = (points[index_i], points[closest_index])
        pair = Pair(points[index_i], points[closest_index], min_distance)
        pairs.append(pair)
    result = Analysis(pairs, operations)
    return result


def closest_pairs_brute_driver(points, filename="pairs.txt"):
    result = closest_pairs_brute(points)
    pairs = result.result
    display_pairs(pairs, filename)

    return result



# ---------- Recursive Method (1.c-d) ----------
'''
# Pseudocode (1.c):
#
#
# List of Pairs = EMPTY LIST
#  Use merge sort to sort Data Set A by x-coordinate 
#  If length of Data Set A < 3:
#    for point1 in A:
#      min_distance = INFINITY
#      for point2 in A:
#        distance = distance(point1, point2) 
#        if distance is less than min_distance
#          update min_distance with new distance
#        create new pair with points comprising min_distance
#        add new pair to list of pairs
#     return the small list of pairs
#  Else: 
#    Recursively find closest pairs (half 1)
#    Recursively find closest pairs (half 2)
#    distance = EMPTY LIST
#    for index 0 -> length of h1 + length of h2:
#      get the smaller distance
#      add the pair/distance to distance
#    return distance
#
# parse pairs out of distance to get list of closest_pairs 
'''



'''
# Recursive Implementation (1.d)
# Description: Find the closest Point to each Point in the Data Set
# Either print the results to console if the size of the data set <= 30
# Else write the results to pairs.txt
'''


# 
# Main function for calculating the closest pairs using the recursive algorithm described above
# @params points Data Set containing a list of Points
# @returns an Analysis object, containing both the list of pairs generated by the recursive algorithm
# as well as a count of the number of distance calculations, for use in complexity analysis
def closest_pairs_recursive(points):
    pairs = []
    operations = 0
    if len(points) < 3:
        return closest_pairs_brute(points)
    else:
        midpoint = len(points) // 2
        left_result = closest_pairs_recursive(points[0:midpoint])
        right_result = closest_pairs_recursive(points[midpoint:])
        operations = left_result.operations + right_result.operations
        left_pairs = left_result.result
        right_pairs = right_result.result
        left_index = 0
        right_index = 0
        while (left_index < len(left_pairs) and right_index < len(right_pairs)):
            left_distance = left_pairs[left_index].distance
            right_distance = right_pairs[right_index].distance
            operations += 1
            if (left_distance < right_distance):
                pairs.append(left_pairs[left_index])
                left_index+=1
            else:
                pairs.append(right_pairs[right_index])
                right_index+=1

        while (left_index < len(left_pairs)):
            pairs.append(left_pairs[left_index])
            left_index+=1

        while (right_index < len(right_pairs)):
            pairs.append(right_pairs[right_index])
            right_index+=1
        
    result = Analysis(pairs, operations)
    return result


def closest_pairs_recursive_driver(points, filename="pairs.txt"):
    result = closest_pairs_recursive(points)
    pairs = result.result
    display_pairs(pairs, filename)

    return result