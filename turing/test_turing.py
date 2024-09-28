import unittest
from turing import *
import re

class UnitTests(unittest.TestCase):
    
    def test_move_forward(self):
        tape = list("ABCDEF")
        expected = "ABCDEF##"
        turing = Turing(tape, 0)
        for e in expected:
            head = turing.get_head()
            self.assertEqual(e, head)
            turing.move_forward()

    def test_move_backward(self):
        tape = list("FEDCBA")
        expected = "ABCDEF##"
        turing = Turing(tape, 0)
        turing.head_index = 5
        for e in expected:
            head = turing.get_head()
            self.assertEqual(e, head)
            turing.move_backward()
    
    def test_transition(self):
        expected = "CORRECT"
        tape = list("MESSAGE")
        states = ['one', 'two', 'three',
                  'four', 'five']
        rules = [
            [START, 'M', 1, "two", "C"],
            ['two', 'E', 1, "three", "O"],
            ['three', 'S', 1, "three", "R"],
            ['three', 'A', 1, "four", "E"],
            ["four", 'G', 1, "five", "C"],
            ["five", 'E', 1, ACCEPT, "T"]

        ]
        turing = Turing(tape, 0)
        turing.add_states_from_list(states)
        turing.add_rules_from_list(rules)
        for e in expected:
            turing.transition()
            prev = turing.tape[turing.head_index-1]
            self.assertEqual(e, prev)
        self.assertTrue(turing.is_halted())

class IntegrationTests(unittest.TestCase):

    def test_simple(self):
        input = "11111#111"
        result = turing_driver(input)
        actual = "".join(result)
        expected = re.compile(r"#*11111#111#11#*")
        self.assertTrue(expected.match(actual))

    def test_left_heavy(self):
        input = "1111111111111111111#111"
        result = turing_driver(input)
        actual = "".join(result)
        expected = re.compile(r"#*1111111111111111111#111#1111111111111111#*")
        self.assertTrue(expected.match(actual))

    def test_right_heavy(self):
        input = "1111#1111111111111111111"
        result = turing_driver(input)
        actual = "".join(result)
        expected = re.compile(r"#*1111#1111111111111111111#111111111111111#*")
        self.assertTrue(expected.match(actual))

    def test_balanced(self):
        input = "1111111111111111111#1111111111111111111"
        result = turing_driver(input)
        actual = "".join(result)
        expected = re.compile(r"#*1111111111111111111#1111111111111111111##*")
        self.assertTrue(expected.match(actual))

    def test_empty(self):
        input = "#"
        result = turing_driver(input)
        self.assertEqual(result, 'REJECT')

    def test_one_operand(self):
        input="11111#"
        result = turing_driver(input)
        self.assertEqual(result, 'REJECT')

if __name__ == '__main__':
    unittest.main()