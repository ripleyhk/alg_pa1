# EN.605.621 Programming Analysis Assignment 1
## Files
### pairs
- **/pairs/main/closest_pairs.py** <- This is where both closest pair algorithms are implemented
- /pairs/objects/analysis.py 
- /pairs/objects/pair.py
- /pairs/objects/point.py
- /pairs/utils/pair_utils.py
- /pairs/pairs.py <- This is the driver for running the closest pair algorithm from the command line
- /pairs/performance_pairs.py <- This is the driver for running closest pair performance analytics from the command line
- /pairs/test_pairs.py <- This is the driver for running closest pair unit and integration tests
### turing
- /turing/performance_turing.py <- This is the driver for running turing performance analytics from the command line
- /turing/test_turing.py <- This is the driver for running turing unit and integration tests
- **/turing/turing.py** <- This is both the driver for and where the turing machine and unary subtraction algorithm are implemented
### General
- PA1_Analysis.pdf <- This is the full writeup for PA1
- README.md <- You're here!
## Build Environment
- OS: Windows 11 Pro
- IDE: VSCode 1.92.2
- Language: Python 3.12.6
## Build and Utilization
All modules utilized by this project are part of the Python Standard Library.
This project uses the following Python modules:
- argparse
- math
- os
- random
- re

### Running the Closest Pairs Algorithm
From /RipleyPA1:
- Run "python .\pairs\pairs.py -h" for help
- Run "python .\pairs\pairs.py brute -n <dataset size>" to run the brute force algorithm on a random dataset
- Run "python .\pairs\pairs.py brute -p <'(x1,y1), (x2,y2)...'"> to run the brute force algorithm on the specified list of points
- Run "python .\pairs\pairs.py brute <n or p> -f <filename>" to run the brute force algorithm and write to a specified file for n > 30
- Run "python .\pairs\pairs.py recursive -n <dataset size>" to run the recursive algorithm on a random dataset
- Run "python .\pairs\pairs.py recursive -p <'(x1,y1), (x2,y2)...'>" to run the recursive algorithm on the specified list of points
- Run "python .\pairs\pairs.py recursive <n or p> -f <filename>" to run the recursive algorithm and write to a specified file for n > 30
- Run "python .\pairs\pairs.py <recursive or brute> <n or p> -a" to run the closest pair algorithm and display performance metrics
### Running Closest Pair Performance Metrics
From /RipleyPA1:
- Run "python .\pairs\performance_pairs.py -h" for help
- Run "python .\pairs\performance_pairs.py" to run both brute-force and recursive closest pair performance metrics on the default list of dataset sizes
- Run "python .\pairs\performance_pairs.py -b -r" to run both brute-force and recursive closest pair performance metrics on the default list of dataset sizes
- Run "python .\pairs\performance_pairs.py -b" to run brute-force closest pair performance metrics on the default list of dataset sizes
- Run "python .\pairs\performance_pairs.py -r" to run recursive closest pair performance metrics on the default list of dataset sizes
- Run "python .\pairs\performance_pairs.py <-b or -r> -n <1 or more input sizes>" to run closest pair performance metrics on datasets of the specified sizes

### Running Closest Pairs Unit and Integration Test
From /RipleyPA1:
- Run "python .\pairs\test_pairs.py" to run unit and integration tests for the closest pair codebase
### Running the DTM Unary Subtraction Algorithm
From /RipleyPA1:
- Run "python .\turing\turing.py -h" for help
- Run "python .\turing\turing.py <'1..#1...'>" to run unary subtraction on the specified string
- Run "python .\turing\turing.py <'1..#1...'> -a " to run unary subtraction on the specified string and display performance metrics
### Running DTM Performance Metrics
From /RipleyPA1:
- Run "python .\turing\performance_turing.py -h" for help
- Run "python .\turing\performance_turing.py" to run DTM performance metrics on the default list of dataset sizes
- Run "python .\turing\performance_turing.py -n <1 or more input sizes>" to run DTM performance metrics on datasets of the specified sizes

### Runing DTM Unit and Integration Tests
From /RipleyPA1:
- Run "python .\turing\test_turing.py" to run unit and integration tests for the DTM codebase
