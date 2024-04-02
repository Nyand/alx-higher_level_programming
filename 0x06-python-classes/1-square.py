#!/usr/bin/python3
"""defining a square"""


class Square:
    """type class square

    Attributes:
    ___size (int): size of a side of the square
    """

    def __init__(self, size):
        """Initialize the square class
        Args:
        param1: size is the type int attribute to make it private
        """
        self.__size = size
