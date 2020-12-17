import collections
from typing import DefaultDict, List

from test_framework import generic_test, test_utils

# Time: n sorts, and n insertions
#       nmlogm to sort all keys where m is max string length
#       n to insert all
#       => O(nmlogm)
# Space: O(n)
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    d = collections.defaultdict(list)
    for s in dictionary:
        d[''.join(sorted(s))].append(s)
    return [ l for l in d.values() if len(l) > 1 ]

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
