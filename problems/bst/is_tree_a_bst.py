from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

# Time: O(n)
# Space: O(h)
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def in_range(tree, low_range=float('-inf'), high_range=float('inf')):
        if not tree:
            return True
        elif low_range <= tree.data <= high_range:
            return (in_range(tree.left, low_range, tree.data) 
                    and in_range(tree.right, tree.data, high_range))
        else:
            return False

    return in_range(tree)

# Inorder traversal       
# Time: O(n)
# Space: O(h)
def is_binary_tree_bst_alternative(tree):
    def inorder_traversal(tree):
        if not tree:
            return True
        elif not inorder_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data > tree.data:
            return False
        prev[0] = tree
        return inorder_traversal(tree.right)

    prev = [None]
    return inorder_traversal(tree)

# BFS 
# Time: O(n) Space: O(n)
# Reduce time when BST property violated at small depth
def is_binary_tree_bst_bfs(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower',
                                                       'upper',))
    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])
    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

if __name__ == '__main__':
    print("BFS:")
    generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_bfs)
    print("Inorder Traversal:")
    generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_alternative)
    print("In Range:")
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
