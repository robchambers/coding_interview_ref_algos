"""lower_case_with_underscores.py"""

import os  # STD lib imports first
import sys  # alphabetical

# 3rd party stuff next, alphabetical

# local stuff last
from .moduleY import spam as ham
from . import moduleY

_a_global_var = 2  # so it won't get imported by 'from foo import *'
_b_global_var = 3

A_CONSTANT = 'ugh.'


# 2 empty lines between top-level funcs + classes
def naming_convention():
    """Write docstrings for ALL public classes, funcs and methods.
    Functions use snake_case.
    """
    if x == 4:  # x is blue <== USEFUL 1-liner comment (2 spaces before #)
        x, y = y, x  # inverse x and y <== USELESS COMMENT (1 space after #)
    c = (a + b) * (a - b)  # operator spacing should improve readability.
    dict['key'] = dict[0] = {'x': 2, 'cat': 'not a dog'}


class NamingConvention(object):
    """First line of a docstring is short and next to the quotes.
    Class and exception names are CapWords.
    Closing quotes are on their own line
    """

    a = 2
    b = 4
    _internal_variable = 3
    class_ = 'foo'  # trailing underscore to avoid conflict with builtin

    # some examples of how to wrap code to conform to 79-columns limit:
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if width == 0 and height == 0 and \
                color == 'red' and emphasis == 'strong' or \
                highlight > 100:
            raise ValueError('sorry, you lose')
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight, y=None)

    # empty lines within method to enhance readability; no set rule
    short_foo_dict = {'loooooooooooooooooooong_element_name': 'cat',
                      'other_element': 'dog'}

    long_foo_dict_with_many_elements = {
        'foo': 'cat',
        'bar': 'dog'
    }

    @classmethod
    def bar(cls):
        """Use cls!"""
        pass

#### LANGUAGE ####
"""
Ops: 10 % 7 = 3; 10 // 3 = 3;  2**3 = 8
OOp: ();  **;  +x, -x, ~x;  *, /, //, %;  +, -;  <<, >>;  &; ^; |; comparison;  not;  and;  or
     P    P                   M    D      A  S       Binary         Comparison   Logical not-and-or
Comp: ==, !=, <>, etc.
Logical: and, or, not  (similar: in, not in)
Binary ops: &, |, ^, ~, <<, >>
"""

"""
string: 
 sets: .ascii_[letters,lowercase,uppercase], .digits, .punctuation, .whitespace
 methods: 
    .capitalize(), .count(sub), .endswith(suffix), .startswith(prefix)
    .find(sub[, start[, end]]) -> (-1 | int), .index(sub[, start[, end]]) -> (Err | int), 
    .isalnum(), .isalpha(), .isdigit(), .islower(), 
    .lower(), .upper()
    .join(iterable), .split(sep), .splitlines(), 
    .replace(old, new[, count]), .strip()
"""
