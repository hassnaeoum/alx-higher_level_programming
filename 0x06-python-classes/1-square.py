#!/usr/bin/python3
""" Square class """


class Square:
    """ class represents a suqare.
    attributes:
        __size (int): the size of the square(private)
    """
    def __init__(self, size):
        """
        Initializes a new instance of the square class.
        args:
            size(int): the size of the square
        """
        self.__size = size
