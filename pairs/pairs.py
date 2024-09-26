import argparse, math
from objects import Point
from main import *
from utils import generate_random_points_list

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Description: Driver for running Closest Pair algorithms on random dataset of input size n
# See "/pairs/main/closest_pairs.py" for algorithm implmentations
'''

if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Closest Pairs", description="Calculate the closest pair of points in a data set")
    parser.add_argument("mode", choices=['brute', 'recursive', 'b', 'r'], help="Algorithm mode")

    group= parser.add_argument_group('Input')
    group_ex = group.add_mutually_exclusive_group()
    group_ex.add_argument("-n", "--size", type=int, help="Size of random dataset to generate")
    group_ex.add_argument("-p", "--points", nargs="*", type=str, help="List of points, formated [(x1,y1), (x2,y2), ...]")
    group_ex.required = True
    parser.add_argument_group(group)

    parser.add_argument("-f", "--filename", nargs='?', default="pairs.txt", help="File to write closest pair data")
    parser.add_argument("-a", "--analytics", action="store_true", help="Show algorithm analytics")
    args=parser.parse_args()
    
    if (args.size):
        points = generate_random_points_list(args.size)
    elif (args.points):
        points = []
        input = args.points
        for index in range(0, len(input), 2):
            x = float(input[index])
            y = float(input[index+1])
            point = Point(x, y)
            points.append(point)
            
    if args.mode=='brute' or args.mode=='b':
        closest_pair_brute_driver(points, args.filename)
    else:
        closest_pair_recursive_driver(points, args.filename)
    if args.analytics:
        analysis = get_analysis()
        print(analysis.operations_str())
