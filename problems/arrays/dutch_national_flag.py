import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# Space: O(1), Time: O(n)
# Single pass instead of 2 pass
def dutch_flag_partitionD(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index] 
    l, e, g = 0, 0, len(A)-1
    while e <= g:
        if A[e] < pivot:
            A[e], A[l] = A[l], A[e]
            l += 1
            e += 1
        elif A[e] > pivot:
            A[e], A[g] = A[g], A[e]
            g -= 1
        else:
            e += 1

# Space: O(1), Time: O(n)
# Similar to B but instead of search for swap, keep track of subarrays
def dutch_flag_partitionC(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

# Space: O(1), Time: O(n^2)
# Last test took a long time.
def dutch_flag_partitionB(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index] 
    for i in range(len(A)):
        # Find/Swap with smaller
        for j in range(i+1,len(A)): # doesn't include i
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break # Stop when reach less than pivot since already correct
        # Find/Swap with larger
        for j in reversed(range(i)): # doesn't include i (i-1 to 0)
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

# Space: extra O(n) , Time: O(n)
def dutch_flag_partitionA(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index] 
    less, equal, greater = [], [], []
    for item in A:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)
        
    A = less + equal + greater
 
@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partitionD, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
