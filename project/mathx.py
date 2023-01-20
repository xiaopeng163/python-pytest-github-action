# -*- coding: utf-8 -*-
"""This module creates three functions to be tested."""


def add(x: int, y: int) -> int:
    """Add two numbers together.

    Args:
                    x (int): first number to add
                    y (int): second number to add

    Returns:
                    int: sum of x and y
    """
    return x + y


def subtract(x: int, y: int) -> int:
    """Subtract one number from another.

    Args:
                    x (int): first number to subtract
                    y (int): second number to subtract

    Returns:
                    int: resut of x subtract y
    """
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply two numbers together.

    Args:
                    x (int): first number in the multiplication
                    y (int): second number in the multiplication

    Returns:
                    int: product of x and y
    """
    return x * y


def divide(x: int, y: int) -> float:
    """Divide two numbers together.

    Args:
                    x (int): first number in the division
                    y (int): second number in the division

    Returns:
                    int: dividend of x and y
    """
    return x / y