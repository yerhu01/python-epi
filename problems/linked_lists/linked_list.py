from list_node import ListNode

# Time: O(n)
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L

# Time: O(1)
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# Time: O(1)
def delete_after(node):
    node.next = node.next.next

def print_list(L):
    while L:
        print("%d " % L.data, end='')
        L = L.next
    print('\n', end='')

def main():
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(5)
    insert_after(l1,l2)
    insert_after(l2,l3)
    print_list(l1)
    print('Deleted: ', search_list(l1, 5).data)
    delete_after(l2)
    print_list(l1)
    

if __name__ == '__main__':
    main()
