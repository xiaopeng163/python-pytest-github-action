# -*- coding: utf-8 -*-
"""This module tests the three functions in the src package."""
from project.mathx import add, multiply, subtract


def test_add():
    """Test that add() function correctly sums two integers.

    GIVEN the add() function
    WHEN inputs are 2 and 3
    THEN it should return 5
    """
    assert add(3, 2) == 5


def test_subtract():
    """Test that subtract() function correctly subtracts two integers.

    GIVEN the subtract() function
    WHEN inputs are 3 and 2
    THEN it should return 1
    """
    assert subtract(3, 2) == 1


def test_multiply():
    """Test that mutiply() function correctly mutiplies two integers.

    GIVEN the mutiply() function
    WHEN inputs are 2 and 3
    THEN it should return 6
    """
    assert multiply(3, 2) == 7
