from typing import List

from test_framework import generic_test

import itertools

# Time: O(n), Space: O(1)
def find_maximum_subarray(A: List[int]) -> int:
    max_seen = running_sum = 0
    for a in A:
        running_sum = max(a, a + running_sum)
        max_seen = max(max_seen, running_sum)
    return max_seen

# Time: O(n), Space: O(1)
def find_maximum_subarray_min(A: List[int]) -> int:
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum) 
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

if __name__ == '__main__':
    print("Remove min array:")
    generic_test.generic_test_main('max_sum_subarray.py',
                                   'max_sum_subarray.tsv',
                                    find_maximum_subarray_min)
    print("Max running sum:")
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
