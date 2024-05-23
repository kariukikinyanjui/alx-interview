#!/usr/bin/python3
'''Define a function isWinner'''


def isWinner(x, nums):
    '''
    Determine the winnder of a prime number game.
    '''
    def is_prime(n):
        '''
        Check if a number is prime

        Parameters:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        '''
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        '''
        Simulate a single round of the game.

        Parameters:
        n(int): The maximum number for this round.

        Returns:
        bool: True if Maria wins this round, False if Ben wins.
        '''
        primes = [i for i in range(2, n+1) if is_prime(i)]
        return len(primes) % 2 == 1

    Maria_wins = sum(game(n) for n in nums)
    Ben_wins = x - Maria_wins

    if Maria_wins > Ben_wins:
        return 'Maria'
    elif Ben_wins > Maria_wins:
        return 'Ben'
    else:
        return None
