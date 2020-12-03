from test_framework import generic_test

# Time: O(1) Space: O(1)
def change_making(cents: int) -> int:
    num_coins = 0
    coins = [100, 50, 25, 10, 5, 1]
    for coin in coins:
        num_coins += cents // coin
        cents %= coin
    return num_coins 

# Time: O(n) Space: O(1)
def change_making_bad(cents: int) -> int:
    num_coins = 0
    coins = [100, 50, 25, 10, 5, 1]
    while cents:
        for coin in coins:
            if cents - coin >= 0:
                cents -= coin
                num_coins += 1
                break
    return num_coins


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
