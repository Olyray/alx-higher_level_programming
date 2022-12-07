#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return list(list(map(lambda a: a*a, num_list)) for num_list in matrix)
