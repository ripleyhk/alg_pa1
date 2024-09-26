'''
# Author: Hannah Ripley
# Date: 09/30/2024
#
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

    def operations_str(self) -> str:
        return "Total Operations= {0}".format(self.operations)

    def __str__(self):
        return "{0}\nTotal Operations= {1}".format(self.result, self.operations)

    def __repr__(self):
        return "{0}\nTotal Operations= {1}".format(self.result, self.operations)