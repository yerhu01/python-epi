from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Iterative implementation
# TODO
def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    pass

# Recursive implementation
# Time: O(n) Space: O(h) where h is n when skewed, logn when complete 
def postorder_traversalr(tree: BinaryTreeNode) -> List[int]:
    def traverse(root):
        if root:
            traverse(root.left)
            traverse(root.right)
            result.append(root.data)
    result = []
    traverse(tree)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversalr))
