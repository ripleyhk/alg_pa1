import math

'''
# Author: Hannah Ripley
# Date: 09/30/2024
#
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