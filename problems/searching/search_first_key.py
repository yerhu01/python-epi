import bisect
from typing import List

from test_framework import generic_test

# Without bisect
# Time: O(logn) Space: O(1)
def search_first_of_k(A: List[int], k: int) -> int:
    L, U, result = 0, len(A)-1, -1
    while L <= U:
        M = L + (U-L)//2
        if A[M] > k:
            U = M - 1
        elif A[M] < k:
            L = M + 1
        else:
            result, U = M, M - 1
    return result

# Pythonic solution
# Time: O(logn), Space: O(1)
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
