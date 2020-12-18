from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

# class BSTNode:
#       def __init__(self, data=None, left=None, right=None):
#               self.data, self.left, self.right = data, left, right

# Time: O(h) Space: O(1)
def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    it = tree
    while it:
        if it.data == key:
            return it
        elif it.data < key:
            it = it.right
        else:
            it = it.left
    return it

# Time: O(h) where h is the height of the tree
# Space: O(h)
def search_bstr(tree: BstNode, key: int) -> Optional[BstNode]:
    if not tree or tree.data == key:
        return tree
    elif tree.data < key:
        return search_bst(tree.right, key)
    else:
        return search_bst(tree.left, key)

# Alternative:
#    return (tree if not tree or tree.data == key else search_bst(
#       tree.left, key) if key < tree.data else search_bst(tree.right, key))
   
   

def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
