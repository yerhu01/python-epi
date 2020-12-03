import functools

from test_framework import generic_test

# Time: O(n)
# Space: O(1)
def fibonacci_bottomup(n: int) -> int:
    if n <= 1:
        return n
    fib_minus_2, fib_minus_1 = 0, 1
    for _ in range(1, n):
        f = fib_minus_1 + fib_minus_2
        fib_minus_2, fib_minus_1 = fib_minus_1, f
    return f

# Time: O(n) Space: O(n)
def fibonacci_cache(n: int) -> int:
    def fib(n, cache={}):
        if n <= 1:
            return n
        elif n not in cache:
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib(n)

# Time: O(n) Space: O(n)
# Store function calls
@functools.lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print("Iterative Bottom Up:")
    generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci_bottomup)
    print("Cache:")
    generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci_cache)
    print("LRU Cache:")
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
