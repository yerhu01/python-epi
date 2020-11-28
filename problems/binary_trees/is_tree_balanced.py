import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Time: O(n) same as Postorder traversal
# Space: O(h) function call stack bounded by height of tree
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))
    
    # Postorder traversal
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base Case

        left = check_balanced(tree.left)
        if not left.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        right = check_balanced(tree.right)
        if not right.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        is_balanced = abs(left.height - right.height) <= 1
        height = max(left.height, right.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
