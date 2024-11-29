#!/usr/bin/python3
"""
   This module defines the function: makeChange
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be made.

    Returns:
        int: Fewest number of coins needed to meet total,
             -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many coins of this denomination as possible
        num_coins += total // coin
        total %= coin

    # If we still have some total left, it means it's not possible to make it
    if total > 0:
        return -1

    return num_coins
