from list_node import ListNode
from test_framework import generic_test

# Time: O(n) Space: O(n)
def reverse_list_stack(head: ListNode) -> ListNode:
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    dummy = ListNode(0)
    tail = dummy
    while nodes:
        tail.next = nodes.pop()
        tail = tail.next
    tail.next = None
    return dummy.next

# Time: O(n) Space: O(1)        
def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
        #tmp1 = dummy.next
        #tmp2 = head.next
        #dummy.next = head
        #head.next = tmp1
        #head = tmp2
    return dummy.next

if __name__ == '__main__':
    print("Stack:")
    generic_test.generic_test_main('reverse_list.py', 'reverse_list.tsv',
                                                                reverse_list_stack)
    print("Constant space:")
    exit(
        generic_test.generic_test_main('reverse_list.py', 'reverse_list.tsv',
                                       reverse_list))
