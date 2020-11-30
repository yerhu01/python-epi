import collections
from typing import DefaultDict, List

from test_framework import generic_test, test_utils

# Time: n sorts, and n insertions
#       nmlogm to sort all keys where m is max string length
#       n to insert all
#       => O(nmlogm)
# Space: O(n)
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # k = sorted string, v = original string
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
    return [
        group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]

# Naive approach:
# Sort a string, compare each string with all other strings to find matches
# Time: O(n^2*mlogm)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
