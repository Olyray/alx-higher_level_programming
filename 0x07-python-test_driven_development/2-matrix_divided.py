#!/usr/bin/python3
"""This module creates a function that divides a matrix"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    
    Parameters:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide the matrix elements by.
    
    Returns:
        list of lists: A new matrix with the divided elements.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If div is not a number.
        TypeError: If rows of matrix do not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    num_cols = len(matrix[0])
    if not all(len(row) == num_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide all elements of the matrix by div and round to 2 decimal places
    result = [[round(val / div, 2) for val in row] for row in matrix]

    return result

