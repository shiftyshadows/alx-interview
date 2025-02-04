#!/usr/bin/python3
"""
This module defines the function: rotate_2d_matrix(matrix).
"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n matrix to rotate.
    Returns:
        None: The function modifies the matrix in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve 90-degree clockwise rotation
    for row in matrix:
        row.reverse()
