#!/usr/bin/python3
"""
   This module defines the function: isWinner.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime removal game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben").
        None: If no winner can be determined.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum n in nums to determine primes up to that value
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Precompute the number of primes up to each index
    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        if primes_count[n] % 2 == 1:  # Odd count of primes => Maria wins
            maria_wins += 1
        else:  # Even count of primes => Ben wins
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
