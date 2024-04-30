#!/usr/bin/python3
'''makeChange function'''


def makeChange(coins, total):
    if total <= 0:
        return 0

    # sort coinds in descending order
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total == 0:
        return num_coins
    else:
        return -1
