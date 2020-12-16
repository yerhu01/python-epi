import heapq
from typing import List, Tuple

from test_framework import generic_test

# Alternative method: recursive merge step from merge sort.

# Time: O(nlogk) where k is number of lists, since each element must 
#       go through a heap of size k
# Space: O(k) additional storage for heap
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []
    iters = [iter(l) for l in sorted_arrays]

    # Initialize heap with first val of all arrays
    for i, it in enumerate(iters):
        val = next(it, None)
        if val is not None:
            heapq.heappush(min_heap, (val, i))

    result = []
    while min_heap:
        smallest, i = heapq.heappop(min_heap)
        result.append(smallest)
        next_val = next(iters[i], None)
        if next_val is not None:
            heapq.heappush(min_heap, (next_val, i))
    return result    

# Brute force (not implemented)
# Concatenate all sequences then sort it O(nlogn) where n is # of elements
  
# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
