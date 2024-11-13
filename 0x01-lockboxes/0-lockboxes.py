#!/usr/bin/python3
"""
   This module defines the function canUnlockAll
"""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list of lists where each sublist
        contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True      # The first box is unlocked
    stack = [0]             # Start with the first box

    # Perform DFS to unlock boxes
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
