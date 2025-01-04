#!/usr/bin/python3
"""
   This module defines the function: isWinner.
"""


def isWinner(x, nums):
    def sieve(n):
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
