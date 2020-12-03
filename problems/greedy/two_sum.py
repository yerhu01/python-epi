from typing import List

from test_framework import generic_test

# Time: O(n) Space: O(1)
def has_two_sum(A: List[int], t: int) -> bool:
    i, j = 0, len(A)-1
    while i <= j: # Can use same entry twice
        if A[i] + A[j] < t:
            i += 1
        elif A[i] + A[j] > t:
            j -= 1
        else:
            return True
    return False

# Hash table, add all into table and test for each -> O(n) and O(n) space
# Bruteforce, nested loop -> O(n^2)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
