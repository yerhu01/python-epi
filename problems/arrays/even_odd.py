# Reorder list of integers such that even entries appear first.
# Solve without allocating additional storage.

# Space: O(1) = variables
# Time: O(n)
def even_odd(A):
    next_even, next_odd = 0, len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

def main():
    A = [1, 52, 33, 20, 18, 43, 9, 26, 81]
    print(A)
    even_odd(A)
    print(A) 

if __name__ == '__main__':
    main()
