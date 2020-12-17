
# iterative
# Time: O(logn), Space: O(1)
def bsearch(t, A):
    L, M, U = 0, 0, len(A)-1
    while L <= U:
        M = L + (U-L)//2 
        if A[M] > t: # search left
            U = M - 1
        elif A[M] < t:
            # search right
            L = M + 1
        else:
            return M
    return -1 

# recursive
# Time: O(logn), Space: O(logn)
def bsearchr(t,A):
    L, U = 0, len(A)-1

    def search(L, U):
        if L > U:
            return -1

        M = L + (U-L)//2 
        if A[M] > t:
            return search(L ,M-1)
        elif A[M] < t:
            return search(M+1,U) 
        else:   
            return M 
    
    return search(L,U) 

def main():
    arr = [ 2, 3, 4, 10, 40 ] 
    print(bsearch(10,arr))
    print(bsearchr(10,arr))

if __name__ == '__main__':
    main()
