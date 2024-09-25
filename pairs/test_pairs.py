import unittest
import os
from pairs import *
from generate_pairs import *


'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Test suite for evaluating correctness for Closest Pairs implementations
'''

class UnitTests(unittest.TestCase):
    
    # Test that display_pairs writes len(pairs) > 30 to file
    def test_write_pairs(self):
        size = 31
        actual = -1
        filename = "testpairs.txt"
        pairs = generate_random_pairs_list(size)

        try:
            display_pairs(pairs, filename)
            actual = count_lines(filename)
            clean_artifact(filename)

        except Exception as e:
            self.fail(str(e))

        self.assertEqual(actual, size)

    # Test that display_pairs does not write len(pairs) <= 30 to file
    def test_print_pairs(self):
        size = 30
        filename = "testpairs.txt"
        pairs = generate_random_pairs_list(size)
        clean_artifact(filename)

        try:
            display_pairs(pairs, filename)
            
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
        actual = round(actual, 2)
        self.assertEqual(actual, expected)


class IntegrationTests(unittest.TestCase):

    #Test the closest pairs brute force algorithm for a data set < 30
    def test_closest_pairs_brute_small(self):
        test_data = generate_closest_pairs_list(20)
        points = test_data.points
        expected = test_data.pairs
        actual = closest_pairs_brute_driver(points)
        self.assertEqual(len(actual), len(expected))
        for pair in actual:
            if (not(pair in expected)):
                self.fail("\n{0} is not a closest pair".format(str(pair)))

    # Test the closest pairs brute force algorithm for a data set > 30
    def test_closest_pairs_brute_medium(self):
        test_data = generate_closest_pairs_list(40)
        points = test_data.points
        expected = test_data.pairs
        actual = closest_pairs_brute_driver(points, "brute_medium.txt")
        clean_artifact("brute_medium.txt")
        self.assertEqual(len(actual), len(expected))
        for pair in actual:
            if (not(pair in expected)):
                self.fail("\n{0} is not a closest pair".format(str(pair)))

    # # Test the closest pairs brute force algorithm for an odd-numbered data set
    # def test_closest_pairs_brute_odd(self):
    #     points = [Point(18.2, 8.7), Point(9.42, 7.94), Point(9.49, 0.68), Point(21.1, 21.1),  Point(83.6, 5.59)]
    #     expected = [ (Point(18.2, 8.7), Point(9.42, 7.94)), (Point(9.42, 7.94), Point(9.49, 0.68)), (Point(9.49, 0.68), Point(9.42, 7.94)),
    #                  (Point(21.1, 21.1), Point(18.2, 8.7)), (Point(83.6, 5.59), Point(21.1, 21.1))]
    #     actual = closest_pairs_brute_driver(points).result
    #     self.assertEqual(len(actual), len(expected))
    #     for pair in actual:
    #         if (not(pair in expected)):
    #             self.fail("\n{0} is not a closest pair".format(str(pair)))

# # Test the closest pairs recursive algorithm for a data set < 30
#     def test_closest_pairs_recursive_small(self):
#         test_data = generate_closest_pairs_list(10)
#         points = test_data.points
#         expected = test_data.pairs
#         actual = closest_pairs_recursive_driver(points).result
#         self.assertEqual(len(actual), len(expected))
#         for pair in actual:
#             if (not(pair in expected)):
#                 self.fail("\n{0} is not a closest pair, \nExpected={1}".format(str(pair), str(expected)))

#     # Test the closest pairs recursive algorithm for a data set > 30
#     def test_closest_pairs_recursive_medium(self):
#         test_data = generate_closest_pairs_list(40)
#         points = test_data.points
#         expected = test_data.pairs
#         actual = closest_pairs_recursive_driver(points, "recursive_medium.txt").result
#         clean_artifact("recursive_medium.txt")
#         self.assertEqual(len(actual), len(expected))
#         for pair in actual:
#             if (not(pair in expected)):
#                 self.fail("\n{0} is not a closest pair".format(str(pair)))

# Test the closest pairs recursive algorithm for an odd-numbered data set
    # def test_closest_pairs_recursive_odd(self):
    #     points = [Point(18.2, 8.7), Point(9.42, 7.94), Point(9.49, 0.68), Point(21.1, 21.1),  Point(83.6, 5.59)]
    #     expected = [ (Point(18.2, 8.7), Point(9.42, 7.94)), (Point(9.42, 7.94), Point(9.49, 0.68)), (Point(9.49, 0.68), Point(9.42, 7.94)),
    #                  (Point(21.1, 21.1), Point(18.2, 8.7)), (Point(83.6, 5.59), Point(21.1, 21.1))]
    #     actual = closest_pairs_recursive_driver(points).result
    #     self.assertEqual(len(actual), len(expected))
    #     for pair in actual:
    #         if (not(pair in expected)):
    #             self.fail("\n{0} is not a closest pair".format(str(pair)))


if __name__ == '__main__':
    unittest.main()