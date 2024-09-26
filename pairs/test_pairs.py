import unittest
import os
from pairs import *
from generate_pairs import *


'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Test suite for evaluating correctness for closest pair implementations
'''

class UnitTests(unittest.TestCase):
    
    # Test that display_pair writes len(point) > 30 to file
    def test_write_pair(self):
        size = 31
        filename = "testpair.txt"
        points = generate_random_points_list(size)
        pair = generate_random_pair()
        try:
            display_pair(points, pair, filename)
        except Exception as e:
            self.fail(str(e))

        file_exists = os.path.isfile(filename)
        clean_artifact(filename)
        self.assertTrue(file_exists)


    # Test that display_pair does not write len(point]) <= 30 to file
    def test_print_pair(self):
        size = 30
        filename = "testpair.txt"
        points = generate_random_points_list(size)
        pair = generate_random_pair()
        clean_artifact(filename)

        try:
            display_pair(points, pair, filename)    
        except Exception as e:
            self.fail(str(e))

        file_exists = os.path.isfile(filename)
        self.assertFalse(file_exists)

    # Test the utility function for calculating distance between Points
    def test_distance(self):
        point1 = Point(12, 34)
        point2 = Point(56, 78)
        expected = 62.23
        actual = calculate_distance(point1, point2)
        self.assertTrue(math.isclose(expected, actual, rel_tol=1e-03))


class IntegrationTests(unittest.TestCase):

    #Test the closest pair brute force algorithm for a data set < 30
    def test_closest_pair_brute_small(self):
        min_dist = 11
        n = 20
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_brute_driver(points)
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

    # Test the closest pair brute force algorithm for a data set > 30
    def test_closest_pair_brute_medium(self):
        min_dist = 0.75
        n = 40
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_brute_driver(points, "brute_medium.txt")
        clean_artifact("brute_medium.txt")
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

    # Test the closest pair brute force algorithm for an odd-numbered data set
    def test_closest_pair_brute_odd(self):
        min_dist = 3
        n = 13
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_brute_driver(points)
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

    #Test the closest pair recursive force algorithm for a data set < 30
    def test_closest_pair_recursive_small(self):
        min_dist = 20
        n = 15
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_recursive_driver(points)
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

    # Test the closest pair recursive algorithm for a data set > 30
    def test_closest_pair_recursive_medium(self):
        min_dist = 0.75
        n = 40
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_recursive_driver(points, "brute_medium.txt")
        clean_artifact("brute_medium.txt")
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

    # Test the closest pair recursive algorithm for an odd-numbered data set
    def test_closest_pair_recursive_odd(self):
        min_dist = 3
        n = 13
        test_data = generate_points_and_pair(n, min_dist)
        points = test_data.points
        expected = test_data.pair
        actual = closest_pair_recursive_driver(points)
        self.assertEqual(expected, actual, "Distance {} != {}".format(expected.distance, actual.distance))

if __name__ == '__main__':
    unittest.main()