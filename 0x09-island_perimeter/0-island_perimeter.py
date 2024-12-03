#!/usr/bin/python3
"""
   This module defines the function: island_perimeter(grid).
"""


def island_perimeter(grid):
    """
       Calculate the perimeter of an island in a grid.

       The grid is represented as a list of lists where:
           - 0 represents water
           - 1 represents land

       Args:
           grid (list of list of int): The grid representation
           of the island.

       Returns:
           int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the current land cell
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
