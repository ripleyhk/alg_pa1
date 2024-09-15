from enum import Enum
'''
# Author: Hannah Ripley
# Date: 09/30/2024
# Problem 2: Deterministic Turing Machine (DTM)
# Description: 
'''
# M = (Γ, Q, s, δ, Σ, b) 
# Γ = a finite set of symbols
# Q = a finite set of states,
# termination on qY and qN
# s = direction to move tape head: -1, +1, or halt
# δ = transition function
# Σ = set of input symbols
# b = blank symbol, #
#
# Γ = {S, E, U, 1, #}

class StateType(Enum):
    NORMAL = "normal"
    START = "start"
    ACCEPT = "accept"
    REJECT = "reject"

class Direction(Enum):
        FORWARD = +1
        BACKWARD = -1
        STAY = 0


class State:
    def __init__ (self, name, state_type: StateType = StateType.NORMAL, rules = {}):
        self.name = name
        self.state_type = state_type
        self.rules = rules

    def get_rule(self, input):
        if (input in self.rules):
            rule = self.rules[input]
        else:
            rule = None
        return rule        
        
    def add_rule(self, input, direction: Direction, next_state):
        self.rules[input] = Rule(direction, next_state)


class Rule:
    def __init__ (self, tape_direction: Direction, next_state: State):
        self.tape_direction = tape_direction
        self.next_state = next_state



'''
# The following structure is used to represent a Turing Machine
#
'''
class Turing:
    def __init__ (self, tape=[], head_index=0, states = {}, curr_state: State = None):
        self.tape = tape
        self.head_index = head_index
        self.curr_state = curr_state
        self.states = states
        if (len(states)) == 0:
            states[StateType.START] = State(StateType.START, StateType.START)
            states[StateType.ACCEPT] = State(StateType.ACCEPT, StateType.ACCEPT)
            states[StateType.REJECT] = State(StateType.REJECT, StateType.REJECT)

    # Get the element at the current head of the tape
    def get_head(self):
        return self.tape[self.head_index]
    
    # Move to the next element of the tape
    def move_forward(self):
        next_index = self.head_index + 1
        if (next_index < len(self.tape)):
            self.head_index = next_index

    # Move to the previous element of the tape
    def move_backward(self):
        prev_index = self.head_index - 1
        if (prev_index >= 0):
            self.head_index = prev_index

    def is_halted(self):
        return (self.curr_state.state_type == StateType.ACCEPT 
             or self.curr_state.state_type == StateType.REJECT)

    def add_rule(self, input, state, direction: Direction, next_state):
        if (state in self.states):
            self.states[state].add_rule(input, direction, next_state)

    # Add a rule, formated as [state name, input, +1/0/-1 direction, next state]
    def add_rule_from_array(self, rule):
        state = self.states[rule[0]]
        state.add_rule(rule[1], rule[2], rule[3])
    
    def add_rules_from_array(self, rules):
        for rule in rules:
            self.add_rule(rule)

    def transition(self):
        head = self.get_head()
        state = self.states[self.curr_state]
        rule = state.get_rule(head)
        if (rule):
            self.curr_state = rule.next_state
            if (rule.direction == Direction.FORWARD):
                self.move_forward()
            elif (rule.direction == Direction.BACKWARD):
                self.move_forward()
        else:
            self.curr_state = self.states(StateType.REJECT)

    def run(self):
        while (not self.is_halted()):
            self.transition()

def turing_driver():
    tape = []
    states = []
    rules = [[]]

    turing = Turing(tape, 0, states)
    turing.add_rules_from_array(rules)
    turing.run()

