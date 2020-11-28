import heapq
import itertools

# O(logk) = Time to add/remove one string from the  heap
# Time: O(nlogk) = Time to process all n strings
#     Can improve by comparing len(new_string) with to skip the insert
#     since lookup is O(1)
# Space: O(k)
def top_k(k, stream):
    # min_heap = [ (len(s), s) for s in stream[:k] ] # for list of strings
    # for if stream is an actual stream of strings instead of list
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for item in stream:
        heapq.heappushpop(min_heap, (len(item), item))
    return [ entry[1] for entry in heapq.nsmallest(k, min_heap)]
    
def main():
    stream = ['123', '1234567891234', '1', '12345', '12345', '12', '1234',
              '12345678912345678', '12345', '123456',
        ]
    result = top_k(5, stream)
    print(result)

if __name__ == '__main__':
    main()
