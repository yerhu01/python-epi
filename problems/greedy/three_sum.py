from typing import List

from test_framework import generic_test
from .two_sum import has_two_sum

# Time: O(nlogn + n^2) = O(n^2)
# Space: O(1)
def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        complement = t - A[i] 
        j, k = i, len(A)-1
        while j <= k:
            if A[j] + A[k] < complement:
                j += 1
            elif A[j] + A[k] > complement:
                k -= 1
            else:
                return True
    return False 

# Bruteforce, 3 nested loops -> Time: O(n^3) Space: O(1)
# Hash Table, iterate over pairs and find complement  
#       -> Time: O(n^2) Space: O(n)

# Same as above except using a function
def has_three_sum_alt(A: List[int], t: int) -> bool:
    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
