from typing import List

class BinaryTreeNode():
    def __init__(self, data='A', left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Time: O(n)
# Space: O(h) b/c function call stack reaches max depth of h
#       min value of h = logn (complete binary tree)
#       max value of h = n (skewed tree)
# If each node had parent field, traversals can be done with O(1) Space
def tree_traversal(root):
    if root:
        #print("Preorder: %s" % root.data)
        tree_traversal(root.left)
        #print("Inorder: %s" % root.data)
        tree_traversal(root.right) 
        print("Postorder: %s" % root.data)

# Recursive implementation
# Time: O(n) Space: O(h) b/c call stack -> O(n) if skewed, O(logn) if complete
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    def traverse(root):
        if root:
            result.append(root.data)
            traverse(root.left)
            traverse(root.right)

    traverse(tree)
    return result

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    def traverse(root):
        if root:
            traverse(root.left)
            result.append(root.data)
            traverse(root.right)

    traverse(tree)
    return result

def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    def traverse(root):
        if root:
            traverse(root.left)
            traverse(root.right)
            result.append(root.data)

    traverse(tree)
    return result

def construct_tree():
    D = BinaryTreeNode('D')
    E = BinaryTreeNode('E')
    C = BinaryTreeNode('C', D, E)
    
    H = BinaryTreeNode('H')
    G = BinaryTreeNode('G', H)
    F = BinaryTreeNode('F', right=G)

    B = BinaryTreeNode('B', C, F)

    M = BinaryTreeNode('M')
    L = BinaryTreeNode('L', right=M)
    N = BinaryTreeNode('N')

    K = BinaryTreeNode('K', L, N)
    J = BinaryTreeNode('J', right=K)

    P = BinaryTreeNode('P')
    O = BinaryTreeNode('O', right=P)

    I = BinaryTreeNode('I', J, O)
    root = BinaryTreeNode('A', B, I)
    return root

def main():
    root = construct_tree()
    # tree_traversal(root)
    print("# Preorder: ABCDEFGHIJKLMNOP")
    print("# Inorder: DCEBFHGAJKLMKNIOP")
    print("# Postorder: DECHGFBMLNKJPOIA")
    print(preorder_traversal(root))
    print(inorder_traversal(root))
    print(postorder_traversal(root))

if __name__ == '__main__':
    main()
