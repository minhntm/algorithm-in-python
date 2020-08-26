"""
Problem Statement:
- Implement a function findKthMax(root,k) which will take a BST and any number
    “k” as an input and return kth maximum number from that tree.
Output:
- Returns kth maximum value from the given tree

Sample Input:
    bst = {
        6 -> 4,9
        4 -> 2,5
        9 -> 8,12
        12 -> 10,14
    }
    where parent -> leftChild,rightChild
    k = 3
Sample Output:
- 10
"""


from Node import Node
from BinarySearchTree import BinarySearchTree


def findKthMax(root, k):
    inorder_tree = list(inorder_traverse(root))
    return inorder_tree[-k]


def inorder_traverse(root):
    if root.leftChild:
        yield from inorder_traverse(root.leftChild)
    yield root.val
    if root.rightChild:
        yield from inorder_traverse(root.rightChild)


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(1)
    BST.insert(133)
    BST.insert(12)
    print(findKthMax(BST.root, 3))
