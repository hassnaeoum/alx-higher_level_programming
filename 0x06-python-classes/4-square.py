#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): the size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): the size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the value of the size attribute.

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the size attribute.

        Parameters:
            value (int): the new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
