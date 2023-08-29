#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): the size of the square (private)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): the size of the square (default 0)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the pos attribute value
        Returns:
            tuple: square's position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of positon attribute.
        args:
            valut(tuple): pos of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square using '#' and the given position. """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
