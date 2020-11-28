import heapq
from typing import List, Tuple

from test_framework import generic_test

# Alternative method: recursive merge step from merge sort.

# Time: O(nlogk) where k is number of lists, since each element must 
#       go through a heap of size k
# Space: O(k) additional storage for heap
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []
    sorted_arrays_iters = [iter(l) for l in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_item = next(it, None)
        if first_item is not None:
            heapq.heappush(min_heap, (first_item, i))

    result = []
    while min_heap:
        # Remove min and put in results
        smallest_item, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_item)

        # insert next element into heap
        next_item = next(smallest_array_iter, None)
        # Make sure to use is not for checking None
        if next_item is not None:
            heapq.heappush(min_heap, (next_item, smallest_array_i))
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
