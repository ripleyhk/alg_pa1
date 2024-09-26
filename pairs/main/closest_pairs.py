from objects import Point, Pair, Analysis
from utils import *

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Problem 1: Closest Pairs
# Description: A suite of algorithms for determing the closest two Points, each defined (x, y), based on distance
'''

# Global data structure for tracking operations for complexity analysis
analysis = Analysis()
def get_analysis():
    return analysis
        
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
def display_pair(points: list[Point], pair: Pair, filename: str):
    if (len(points) <= 30):
        print_pair(points, pair)
    else:
        write_pair(points, pair, filename)

# Print closest pair to console
# @param points list of all input points
# @param pair of closest two points
def print_pair(points: list[Point], pair: Pair):
    print("For Data Set:")
    print("{}".format(points))
    pretty_distance = round(pair.distance, 2)
    print("Closest Pair= {}\nDistance={}\n".format(pair, pretty_distance))

# Write closest pair to file
# @param points list of all input points
# @param pair of closest two points
# @param filename name of file to write result to
def write_pair(points: list[Point], pair: Pair, filename: str):
    f = open(filename, "w")
    f.write("For Data Set:\n")
    f.write("{}\n".format(points))
    pretty_distance = round(pair.distance, 2)
    f.write("Closest Pair= {}\nDistance={}\n".format(pair, pretty_distance))
    f.close()

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
def closest_pair_brute(points: list[Point]) -> Pair:
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

def closest_pair_brute_driver(points: list[Point], filename="pair.txt") -> Pair:
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
def closest_pair_recursive(points: list[Point]) -> Pair:
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

        # Uncommon case where all points are near midpoint:
        # Use brute force to prevent infinite loop
        if (len(points_b) == len(points)):
            pair_b = closest_pair_brute(points_b)
        # Typical case: proceed recursively
        else:
            pair_b = closest_pair_recursive(points_b)

        if (pair_b.distance < min_pair.distance):
            min_pair = pair_b
    analysis.result = min_pair
    return min_pair

def closest_pair_recursive_driver(points: list[Point], filename="pairs.txt"):
    analysis.operations = 0
    sorted_points = merge_sort(points)
    pair = closest_pair_recursive(sorted_points)
    display_pair(sorted_points, pair, filename)
    return pair

#
# Get the list of points that surround the midpoint
# i.e. closer than closest pair's distance
#
# @param points Data Set containing the list of Points
# @param closest_pair the current closest pair (and its distance)
# @returns the list of points surrounding the midpoint (that may be part of a bisecting pair)
#
def get_bisecting_points(points: list[Point], closest_pair: Pair) -> list[Point]:   
    bisecting_points = []
    middle = len(points)//2
    midpoint = points[middle]
    for point in points:
        distance = abs(midpoint.x - point.x)
        if (distance < closest_pair.distance):
            bisecting_points.append(point)
    
    return bisecting_points

#
# Implementation of the merge sort algorithm
# @param points input list of points to sort by x
# @returns sorted list of points
def merge_sort(points: list[Point]) -> list[Point]:
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
        if (point_l.x < point_r.x):
            sorted.append(point_l)
            index_l+=1
        else:
            sorted.append(point_r)
            index_r+=1
    while (index_l < len(points_l)):
        analysis.operations+=1
        point_l = points_l[index_l]
        sorted.append(point_l)
        index_l+=1
    while (index_r < len(points_r)):
        analysis.operations+=1
        point_r = points_r[index_r]
        sorted.append(point_r)
        index_r+=1
    return sorted