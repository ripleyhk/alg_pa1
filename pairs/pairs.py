import math

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Problem 1: Closest Pairs
# Description: A suite of algorithms for determing the closest two Points, each defined (x, y), based on distance
'''

# ---------- Display Functions ----------
'''
# The following functions are used to display the result of a pairing algorithm,
# either to the console/terminal, for input <= 30
# or to an output file
#
# This functionality is not being evaluated for running time complexity
'''

# Display pair, either by printing to console (points list length <= 30)
# @param points list of all input points
# @param pair of closest two points
# @param filename name of file to write result to
# or by writing to a file
def display_pair(points, pair, filename):
    if (len(points) <= 30):
        print_pair(points, pair)
    else:
        write_pair(points, pair, filename)

# Print closest pair to console
# @param points list of all input points
# @param pair of closest two points
def print_pair(points, pair):
    print("For Data Set:")
    print("{}".format(points))
    pretty_distance = round(pair.distance, 2)
    print("Closest Pair= {}\n Distance={}\n".format(pair, pretty_distance))

# Write closest pair to file
# @param points list of all input points
# @param pair of closest two points
# @param filename name of file to write result to
def write_pair(points, pair, filename):
    f = open(filename, "w")
    f.write("For Data Set:\n")
    f.write("{}\n".format(points))
    pretty_distance = round(pair.distance, 2)
    f.write("Closest Pair= {}\n Distance={}\n".format(pair, pretty_distance))
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
        pretty_x = round(self.x, 2)
        pretty_y = round(self.y, 2)
        return "[{0},{1}]".format(pretty_x, pretty_y)

    def __repr__(self):
        pretty_x = round(self.x, 2)
        pretty_y = round(self.y, 2)
        return "[{0},{1}]".format(pretty_x, pretty_y)

    def __eq__(self, other):
        return (math.isclose(self.x, other.x)) and (math.isclose(self.y, other.y))
    
'''
# The following structure is used to represent a Pair of points and their distance
#
# This functionality is not being evaluated for running time complexity
'''
class Pair:
    def __init__ (self, point1: Point=None, point2: Point=None, distance=math.inf):
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
        return ((self.point1 == other.point1 and self.point2 == other.point2) or
                (self.point1 == other.point2 and self.point2 == other.point1))
'''
# The following structure is used to hold both the result and operation count for a particular
# execution of a function, for use in complexity analysis
#
# This functionality is not being evaluated for running time complexity
'''
class Analysis:
    def __init__ (self, result=None, operations=0, space=0):
        self.result = result
        self.operations = operations
        self.space = space

    def reset(self):
        self.result = None
        self.operations = 0

    def __str__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)

    def __repr__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)

analysis = Analysis()
def get_analysis():
    return analysis
        
    
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
def calculate_distance(point1: Point, point2: Point):
    delta_x2 = math.pow(point2.x - point1.x, 2)
    delta_y2 = math.pow(point2.y - point1.y, 2)
    distance = math.sqrt(delta_x2 + delta_y2)
    return distance


# ---------- Brute Force Method (1.a-b) ----------
'''
# Pseudocode (1.a):
#
# initial minimum distance = INFINITY (so any actual distance will be smaller)
# initial closest pair = UNDEFINED (because no comparisons have been made yet)
# For index1 starting at 0 -> length of Data Set A:
#   For index2 starting at 0 -> length of Data Set A:
#       skip over index1 == index2 (because the Point should not consider itself as a closet Point)
#       distance = euclidian distance(Point at index1, Point at index2)
#       if distance is smaller than the current mimimum distance:
#           update minimum distance = distance
#           update closest pair = (point at index1, point at index2)
# return (closest pair, minimum distance)
'''

'''
# Brute Force Implementation (1.b)
# Description: Find the closest pair of points in a data set
# Either print the results to console if the size of the data set <= 30
# Else write the results to pair.txt
'''

# 
# Main function for calculating the closest pair of points using the brute force algorithm described above
# @param points Data Set containing a list of Points
# @returns the pair of closest two points and their distance
def closest_pair_brute(points) -> Pair:
    min_pair = Pair()
    for index_i in range(len(points)):
        for index_j in range(len(points)):
            if (index_i == index_j): 
                continue
            '''
            # In order to evaluate the complexity of this algorithm, we will be
            # counting the number of times the distance must be calculated between
            # any two Points
            '''
            distance = calculate_distance(points[index_i], points[index_j])
            analysis.operations += 1
            if (distance < min_pair.distance):
                min_pair.point1 = points[index_i]
                min_pair.point2 = points[index_j]
                min_pair.distance = distance
    analysis.result = min_pair
    return min_pair


def closest_pair_brute_driver(points, filename="pair.txt") -> Pair:
    analysis.operations = 0
    pair = closest_pair_brute(points)
    display_pair(points, pair, filename)
    return pair



# ---------- Recursive Method (1.c-d) ----------
'''
# Pseudocode (1.c):
#
# Use merge sort to sort Data Set A by x
# 
# If length of Data Set A <=3:
#   return closest_pair_brute(Data Set A)
# Else:
#   left pair,  dist = closest_pair(first half of Data Set A)
#   right pair, dist = closest_pair(second half of Data Set A)
#   if left dist < right dist:
#       min pair, dist = left pair, dist
#   else:
#       min pair, dist = right pair, dist
# midpoint = Data Set A [middle index]
# bisecting points = every point closer to the midpoint than the current min dist
# bisecting pair, dist = closest_pair(bisecting points)
# if bisecting dist < min dist:
#  return bisecting pair, dist
# else:
#   return min pair, dist
'''



'''
# Recursive Implementation (1.d)
# Description: Find the closest pair of points in a data set
# Either print the results to console if the size of the data set <= 30
# Else write the results to pairs.txt
'''


# 
# Main function for calculating the closest pair of points using the recursive algorithm described above
# @param points Data Set containing a list of Points
# @returns the pair of closest two points and their distance
def closest_pair_recursive(points) -> Pair:
    analysis.operations+=1
    min_pair = Pair()
    if (len(points) <= 3):
        min_pair = closest_pair_brute(points)
    else:
        middle = len(points)//2
        points_l = points[:middle]
        points_r = points[middle:]
        pair_l = closest_pair_recursive(points_l)
        pair_r = closest_pair_recursive(points_r)
        if (pair_l.distance < pair_r.distance):
            min_pair = pair_l
        else:
            min_pair = pair_r
        points_b = get_bisecting_points(points, min_pair)

        # If all points bisect, do brute force to prevent infinite loop
        if (len(points_b) == len(points)):
            pair_b = closest_pair_brute(points_b)
        # Otherwise, proceed using recursion
        else:
            pair_b = closest_pair_recursive(points_b)

        if (pair_b.distance < min_pair.distance):
            min_pair = pair_b
    analysis.result = min_pair
    return min_pair


#
# Get the list of points that surround the midpoint
# i.e. closer than closest pair's distance
# Points must exist on both sides of midpoint, else return empty list
# @param points Data Set containing the list of Points
# @param closest_pair the current closest pair (and its distance)
# @returns the list of points surrounding the midpoint (that may be part of a bisecting pair)
#
def get_bisecting_points(points: list[Point], closest_pair: Pair):   
    bisecting_points = []
    bisect_left = False
    bisect_right = False

    middle = len(points)//2
    midpoint = points[middle]

    for point in points[:middle]:
        analysis.operations+=1 
        midpoint.y = point.y
        distance = calculate_distance(midpoint, point)
        if (distance < closest_pair.distance):
            bisecting_points.append(point)
            bisect_left = True

    for point in points[middle:]: 
        analysis.operations +=1
        midpoint.y = point.y
        distance = calculate_distance(midpoint, point)
        if (distance < closest_pair.distance):
            bisecting_points.append(point)
            bisect_right = True

    # Points must bisect the midpoint
    if (not(bisect_left and bisect_right)):
        return []
    else:
        return bisecting_points

def merge_sort(points, sort_on="x") -> list[Point]:
    analysis.operations+=1
    if (len(points) < 2):
        return points
    sorted = []
    midpoint = len(points)//2
    points_l = merge_sort(points[:midpoint])
    points_r = merge_sort(points[midpoint:])
    index_l = 0
    index_r = 0
    while (index_l < len(points_l) and index_r < len(points_r)):
        analysis.operations+=1
        point_l = points_l[index_l]
        point_r = points_r[index_r]
        if (point_l.__getattribute__(sort_on) < point_r.__getattribute__(sort_on)):
            sorted.append(point_l)
            index_l+=1
        else:
            sorted.append(point_r)
            index_r+=1
    while (index_l < len(points_l)):
        analysis.operations+=1
        sorted.append(point_l)
        index_l+=1
    while (index_r < len(points_r)):
        analysis.operations+=1
        sorted.append(point_r)
        index_r+=1
    return sorted

def closest_pair_recursive_driver(points, filename="pairs.txt"):
    analysis.operations = 0
    pair = closest_pair_recursive(points)
    sorted_points = merge_sort(points, "x")
    display_pair(sorted_points, pair, filename)
    return pair