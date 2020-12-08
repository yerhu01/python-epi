import functools
import string

from test_framework import generic_test

# Time: O(n + nlogb2 b1))
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    deci = 0
    neg = False
    # Convert b1 string to decimal
    for c in num_as_string:
        if c == '-':
            neg = True
            continue
        deci *= b1
        deci += string.hexdigits.index(c.lower())
    # Convert decimal to b2 string
    result = []
    while True:
        result.append(string.hexdigits[deci % b2].upper())
        deci //= b2
        if deci == 0:
            break
    return ( '-' if neg else '') + ''.join(reversed(result))

    
def convert_baseB(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
