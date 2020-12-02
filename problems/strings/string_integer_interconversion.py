import functools
import string

from test_framework import generic_test
from test_framework.test_failure import TestFailure

# Time: O(n)
def int_to_string(x: int) -> str:
    neg = False
    if x < 0:
        x, neg = -x, True
        
    s = []
    while True:
        s.append('%d' % (x % 10)) # s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    return  ('-' if neg else '') + ''.join(reversed(s)) 

# Time: O(n)
def string_to_int(s: str) -> int:
    result = 0
    neg = False
    for c in s:
        if c == '-':
            neg = True
            continue
        if c == '+':
            continue
        result *= 10
        result += '0123456789'.index(c) # string.digits.index(c)
    if neg:
        result *= -1
    return result
#    return (-1 if s[0] == '-' else 1) * functools.reduce(
#        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
#        s[s[0] in '-+':], 0)

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
