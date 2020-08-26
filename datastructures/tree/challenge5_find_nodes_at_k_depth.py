from Node import Node
from BinarySearchTree import BinarySearchTree


def findKNodes(root, k):
    result = []
    findKDepth(root, k, result)
    return result


def findKDepth(root, k, result):
    if k == 0:
        result.append(root.val)
    if root.leftChild:
        findKDepth(root.leftChild, k - 1, result)
    if root.rightChild:
        findKDepth(root.rightChild, k - 1, result)


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    print(findKNodes(BST.root, 2))
