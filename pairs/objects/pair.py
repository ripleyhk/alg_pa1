import math
from objects import Point

'''
# Author: Hannah Ripley
# Date: 09/30/2024
#
# The following structure is used to represent a Pair of points and their distance
#
# This functionality is not being evaluated for running time complexity
'''
class Pair:
    def __init__ (self, point1: Point=None, point2: Point=None, distance=math.inf):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

    def get_pair(self) -> tuple[Point, Point]:
        return (self.point1, self.point2)

    def __str__(self):
        return "({0}, {1})".format(self.point1, self.point2)

    def __repr__(self):
        return "({0}, {1})".format(self.point1, self.point2)

    def __eq__(self, other):
        return ((self.point1 == other.point1 and self.point2 == other.point2) or
                (self.point1 == other.point2 and self.point2 == other.point1))