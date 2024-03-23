#!/usr/bin/python3
"""
A functions that takes one argument 'n' which represents
the number of H characters we want to achieve
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor += 1

    return operations
