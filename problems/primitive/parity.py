from test_framework import generic_test

# Computing the parity of a word.
# -Return 1 if number of 1's in the word is odd, otherwise 0.


# TODO
def parityC(x: int) -> int:
    return 0

# Dropping lowest set bit method x&(x-1) 
# k = # of bits set to 1, Time: O(k)
def parityB(x: int) -> int:
    result = 0
    while(x):
        result ^= 1 # Keep track if even/odd
        x &= x - 1  # Keep dropping the lowest set bit of x
    return result

# Bruteforce Time: O(n) where n is the word size.
def parityA(x: int) -> int:
    result = 0
    while(x):
        result ^= x & 1
        x >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parityB))
