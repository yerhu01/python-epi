import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Time: O(n) Space: O(1)
def replace_and_remove(size: int, s: List[str]) -> int:
    # Forward iteration: remove b's while counting a's
    fwd, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[fwd] = s[i]
            fwd += 1
        if s[i] == 'a':
            a_count += 1
    
    # Backward iteration: replace a's with 2 d's
    i = fwd - 1
    bwd = fwd - 1 + a_count
    final_size = bwd + 1
    while i >= 0:
        if s[i] == 'a':
            s[bwd-1:bwd+1] = 'dd'
            bwd -= 2
        else:
            s[bwd] = s[i]
            bwd -= 1
        i -= 1
    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
