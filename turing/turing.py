import argparse

'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Problem 2: Deterministic Turing Machine (DTM)
# Description: A rule-agnostic DTM and a ruleset to calculate unary subtraction
# on an input string of two operands, formatted: "1+#1+"
'''

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

    def operations_str(self):
        return "Total Operations={0}".format(self.operations)

    def space_str(self):
        return "Tape Size={0}".format(self.space)    

    def __str__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)

    def __repr__(self):
        return "{0}\nTotal Operations={1}".format(result, operations)

analysis = Analysis()
def get_analysis():
    return analysis
        

# state types
NORMAL = "normal"
START = "start"
ACCEPT = "accept"
REJECT = "reject"

# tape directions
FORWARD = +1
BACKWARD = -1
STAY = 0

'''
# The following represents a Turing machine state and available
# transitions from the state to other states
#
'''
class State:
    def __init__ (self, name, state_type = NORMAL, rules = {}):
        self.name = name
        self.state_type = state_type
        self.rules = rules

    def get_rule(self, input):
        if (input in self.rules):
            rule = self.rules[input]
        else:
            rule = None
        return rule        
        
    def add_rule(self, input, direction, next_state, symbol):
        self.rules[input] = Rule(direction, next_state, symbol)

    def __str__(self):
        return str(self.name)

'''
# The following structure represents a transition rule
#
'''
class Rule:
    def __init__ (self, direction, next_state: State, symbol):
        self.direction = direction
        self.next_state = next_state
        self.symbol = symbol

    def __str__(self):
        return "Move tape= {0}, Move to State={1}, Replace Head with={2}".format(
            self.direction, self.next_state, self.symbol)

'''
# 
# The following structure is used to represent a Turing Machine
#
'''
class Turing:
    '''
    # A Turing Machine Constructor
    # @params tape a list of character strings for processing
    # @params head_index the starting index of the turing head
    # @states an optional dictionary of state names and objects
    '''
    def __init__ (self, tape=[], head_index=0, states = {}):
        self.tape = tape
        self.head_index = head_index
        self.states = states
        if (len(states)) == 0:
            states[START] = State(START, START)
            states[ACCEPT] = State(ACCEPT, ACCEPT)
            states[REJECT] = State(REJECT, REJECT)
        self.curr_state = states[START]

    # Get the element at the current head of the tape
    def get_head(self):
        return self.tape[self.head_index]
    
    # Update the tape head with the symbol from the transition rule
    def update_head(self, symbol):
        self.tape[self.head_index] = symbol
    
    # Move to the next element of the tape
    def move_forward(self):
        self.head_index += 1
        if (self.head_index == len(self.tape)):
            self.tape.append('#')

    # Move to the previous element of the tape
    def move_backward(self):
        self.head_index -= 1
        if (self.head_index < 0):
            self.tape.insert(0, '#')
            self.head_index = 0

    def is_halted(self):
        return (self.curr_state.state_type == ACCEPT 
             or self.curr_state.state_type == REJECT)

    def add_state(self, name, state_type=NORMAL, rules=None):
        state = State(name, state_type, rules)
        self.states[name] = state

    # Add a list of states, optionally also their types and transition rules
    def add_states_from_list(self, names, state_types=None, rules=None):
        for index in range(0, len(names)):
            name = names[index]
            state_type = state_types[index] if state_types else NORMAL
            rule = rules[index] if rules else {}
            self.add_state(name, state_type, rule)
    
    def add_rule(self, input, state, direction, next_state, symbol):
        if (state in self.states):
            self.states[state].add_rule(input, direction, next_state, symbol)

    # Add a rule, formated as [state name, input, +1/0/-1 direction, next state, symbol]
    def add_rule_from_list(self, rule):
        state = self.states[rule[0]]
        next_state = self.states[rule[3]]
        state.add_rule(rule[1], rule[2], next_state, rule[4])
    
    def add_rules_from_list(self, rules):
        for rule in rules:
            self.add_rule_from_list(rule)

    # Transition the turing machine head, base on the current state,
    # head input, and ruleset
    def transition(self):
        analysis.operations+=1
        head = self.get_head()
        rule = self.curr_state.get_rule(head)
        if (rule):
            self.curr_state = rule.next_state
            self.update_head(rule.symbol)
            if (rule.direction == FORWARD):
                self.move_forward()
            elif (rule.direction == BACKWARD):
                self.move_backward()
        else:
            self.curr_state = self.states[REJECT]

    # Transition on tape input until state is ACCEPT or REJECT
    def run(self):
        while (not self.is_halted()):
            self.transition()
        if (self.curr_state.state_type == ACCEPT):
            return self.tape
        else:
            return "REJECT"

    # Utility function for testing transitions    
    def print_debug(self):
        print("Tape= {0}".format(self.tape))
        print("Head= {0} ({1})".format(self.get_head(), self.head_index))
        print("State= {0}".format(self.curr_state))

'''
# The following driver converts a string input to a character list
# Then runs the turing machine using a ruleset for unary subtraction
# It returns the resulting tape char list
'''
def turing_driver(input):
    tape = list(input)
    turing = Turing(tape, 0)
    states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", 
              "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18"]
    # rule format: [state name, input, +1/0/-1 direction, next state, symbol]
    rules = [
        [START, '1', 1, "q0", 'S'],
        ["q0", '1', 1, "q0", '1'],
        ["q0", '#', 1, "q1", '#'],
        ["q1", 'X', 1, "q2", 'X'],
        ["q2", 'X', 1, "q2", 'X'],
        ["q2", '#', -1, "q6", '#'],
        ["q1", '1', -1, "q3", 'X'],
        ["q2", '1', -1, "q3", 'X'],
        ["q3", 'X', -1, "q3", 'X'],
        ["q3", '#', -1, "q4", '#'],
        ["q4", 'X', -1, "q4", 'X'],
        ["q4", '1', 1, "q5", 'X'],
        ["q4", 'S', 0, "q7", 'X'],
        ["q4", "#", 1, "q7", '#'],
        ["q5", 'X', 1, "q5", 'X'],
        ["q5", '#', 1, "q1", '#'],

        ["q6", 'X', -1, "q6", 'X'],
        ["q6", '#', -1, "q7", '#'],
        ["q7", 'X', -1, "q7", 'X'],
        ["q7", '1', -1, "q7", '1'],
        ["q7", 'S', -1, "q7", '1'],
        ["q7", '#', 1, "q8", 'Y'],

        ["q8", "X", 1, "q8", "X"],
        ["q9", "X", 1, "q9", "X"],
        ["q8", "1", 1, "q9", "X"],
        ["q9", "1", 1, "q9", "1"],
        ["q8", "#", 1, "q10", "#"],
        ["q9", "#", 1, "q11", "#"],

        ["q10", "X", 1, "q10", "X"],
        ["q11", "X", 1, "q11", "X"],
        ["q10", "1", 1, "q11", "X"],
        ["q11", "1", 1, "q11", "1"],
        ["q10", "#", 0, "q14", "#"],
        ["q11", "#", 1, "q12", "#"],

        ["q12", "X", 1, "q12", "X"],
        ["q12", "#", -1, "q13", "X"],

        ["q13", "X", -1, "q13", "X"],
        ["q13", "#", -1, "q14", "#"],
        
        ["q14", "X", -1, "q14", "X"],
        ["q14", "1", 1, "q11", "X"],
        ["q14", "#", -1, "q15", "#"],

        ["q15", "X", -1, "q15", "X"],
        ["q15", "1", 1, "q9", "X"],
        ["q15", "Y", 1, "q16", "#"],
        ["q15", "#", -1, "q15", "#"],
   
        ["q16", "X", 1, "q16", "1"],
        ["q16", "#", 1, "q17", "#"],
        ["q17", "X", 1, "q17", "1"],
        ["q17", "#", 1, "q18", "#"],
        ["q18", "X", 1, "q18", "1"],
        ["q18", "#", 0, ACCEPT, "#"]
    ]
    
    turing.add_states_from_list(states)
    turing.add_rules_from_list(rules)
    result = turing.run()
    analysis.result = result
    analysis.space = len(turing.tape)
    return result

if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Unary Subtraction DTM", description="Subtract two unary numbers using a deterministic turing machine")
    parser.add_argument("input", type=str, help="Tape input for DTM, formatted <some number of 1s>#<some number of 1s>")
    parser.add_argument("-a", "--analytics", action="store_true", help="Show algorithm analytics")
    args=parser.parse_args()
    
    result = turing_driver(args.input)
    print(result)

    if args.analytics:
        print(analysis.operations_str())
        print(analysis.space_str())