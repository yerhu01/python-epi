from test_framework import generic_test

# Time: O(logk) Space: O(1)
def square_root(k: int) -> int:
    l, r = 0, k
    
    while l <= r:
        m = l + (r-l)//2
        square = m * m
        if square == k:
            return m
        elif square < k:
            l = m+1
        else:
            r = m-1 
    return l-1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
