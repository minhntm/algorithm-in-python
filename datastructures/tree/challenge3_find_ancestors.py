"""
Problem Statement:
- Implement the findAncestors(root, k) function which will find the ancestors
    of the node whose value is “k”. Here root is the root node of a binary
    search tree and k is an integer value of node whose ancestors you need to
    find. An illustration is also given. Your code is evaluated on the tree
    given in the example.

Output:
- Returns all the ancestors of k in the binary tree in a Python list.

Sample Input:
    bst = {
        6 -> 4,9
        4 -> 2,5
        9 -> 8,12
        12 -> 10,14
    }
    where parent -> leftChild,rightChild
    k = 10
Sample Output:
- [12,9,6]
"""


from Node import Node
from BinarySearchTree import BinarySearchTree


# def findAncestors(root, k):
#     ancestors = []
#     findK(root, k, ancestors)
#     return ancestors

# def findK(root, k, ancestors):
#     if not root:
#         return False
#     if root.val == k:
#         return True
#     if findK(root.leftChild, k, ancestors) or findK(root.rightChild, k, ancestors):
#         ancestors.append(root.val)
#         return True
#     return False


def findAncestors(root, k):
    ancestors = []
    current = root

    while current:
        if current.val > k:
            ancestors.append(current.val)
            current = current.leftChild
        elif current.val < k:
            ancestors.append(current.val)
            current = current.rightChild
        else:
            return ancestors[::-1]

    return []


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(1)
    BST.insert(133)
    BST.insert(12)
    print(findAncestors(BST.root, 12))
