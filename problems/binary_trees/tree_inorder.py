from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Iterative Implementation
# TODO
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    pass

# Recursive Implementation
# Time: O(n) Space: O(h)  where h is n if skewed tree, logn if complete
def inorder_traversalr(tree: BinaryTreeNode) -> List[int]:
    def traverse(root):
        if root:
            traverse(root.left)
            result.append(root.data)
            traverse(root.right)
    result = []
    traverse(tree)
    return result
        
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversalr))
