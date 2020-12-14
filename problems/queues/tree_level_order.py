from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# Time: O(n) Space: O(m) where m is max number of nodes at any depth
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return []

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([node.data for node in curr_depth_nodes]) 
        curr_depth_nodes = [
            child
            for node in curr_depth_nodes for child in (node.left, node.right)
            if child
        ] 
    return result 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
