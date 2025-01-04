#!/usr/bin/python3
"""
   This module defines the function: isWinner.
"""


def isWinner(x, nums):
    """
       Determines the winner of multiple rounds of a game
       where Maria and Ben take turns picking prime numbers
       and removing them and their multiples from a set of
       consecutive integers starting from 1 up to and including n.

       Parameters:
        x (int): The number of rounds.
        nums (list of int): An array of n values, where each
                            n represents the upper limit of the
                            set for each round.

       Returns:
        str: The name of the player that won the most
             rounds ("Maria" or "Ben").
        If the winner cannot be determined, returns None.
    """
    def sieve(n):
        """
           Generates all prime numbers up to n using the Sieve
           of Eratosthenes.

           Parameters:
            n (int): The upper limit to generate prime numbers.

           Returns:
            list of int: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n, primes):
        """
           Simulates a single round of the game.

           Parameters:
            n (int): The upper limit of the set of consecutive integers.
            primes (list of int): A list of prime numbers up to
                                  the maximum n in the input list.

           Returns:
            int: 0 if Maria wins, 1 if Ben wins.
        """
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        while True:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    move_made = True
                    break
            if not move_made:
                return 1 - turn  # The player who cannot make a move loses
            turn = 1 - turn

    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
