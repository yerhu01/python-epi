from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Iterative implementation
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    #TODO
    pass


# Recursive implementation
# Time: O(n) Space: O(h) b/c call stack -> O(n) if skewed, O(logn) if complete
def preorder_traversalr(tree: BinaryTreeNode) -> List[int]:
    def traverse(root):
        if root:
            result.append(root.data)
            traverse(root.left)
            traverse(root.right)
    result = []
    traverse(tree)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversalr))
