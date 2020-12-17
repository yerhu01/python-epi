from typing import List

from test_framework import generic_test
import bisect

# 2 pointers
# Time: O(m+n)
def intersect_two_sorted_arraysA(A: List[int], B: List[int]) -> List[int]:
    i, j, intersect  = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersect.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersect

# Use Binary search
# Time: O(mlogn) where m is the length of the shorter array
# This solution is faster than above if one set is smaller than the other
def intersect_two_sorted_arraysB(A: List[int], B: List[int]) -> List[int]:
    if len(B) < len(A):
        A, B = B, A
    
    def is_present(x):
        i = bisect.bisect_left(B, x)
        return i < len(B) and B[i] == x
    
    return [
            a for i, a in enumerate(A)
            if (i == 0  or a != A[i-1] ) and is_present(a)
    ]


# Bruteforce
# Time: O(mn) where m and n are the lengths of two arrays
# Space: O(n)
def intersect_two_sorted_arraysC(A: List[int], B: List[int]) -> List[int]:
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and a in B]

# fastest
def intersect_two_sorted_arraysD(A: List[int], B: List[int]) -> List[int]:
    return sorted(list(set(A) & set(B)))

if __name__ == '__main__':
    print("Bruteforce O(mn):")
    generic_test.generic_test_main('intersect_sorted_arrays.py',
                                    'intersect_sorted_arrays.tsv',
                                    intersect_two_sorted_arraysC)
    print("Binary Search O(nlogm):")
    generic_test.generic_test_main('intersect_sorted_arrays.py',
                                    'intersect_sorted_arrays.tsv',
                                    intersect_two_sorted_arraysB)
    print("2 Pointers O(n+m):")
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arraysA))
