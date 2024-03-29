#!/usr/bin/python3
"""A module that provides a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix

    Args:
        matrix (list): given matrix
        div (int): number to divide the matrix by

    Returns:
        list: a new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    for item in matrix:
        if isinstance(item, list):
            for element in item:
                if not isinstance(element, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) " +
                        "of integers/floats"
                        )
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for j in range(len(matrix)):
        new_matrix = [
            list(
                map(lambda x: round(x / div, 2), row)
                ) for row in matrix
                ]
    return new_matrix
