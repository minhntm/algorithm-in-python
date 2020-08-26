from Node import Node
from BinarySearchTree import BinarySearchTree


def findHeight(root):
    if not root:
        return 0
    if not root.leftChild and not root.rightChild:
        return 0
    return 1 + max(findHeight(root.leftChild), findHeight(root.rightChild))


if __name__ == "__main__":
    BST = BinarySearchTree(6)
    BST.insert(4)
    BST.insert(9)
    BST.insert(5)
    BST.insert(2)
    BST.insert(8)
    BST.insert(12)
    BST.insert(10)
    BST.insert(14)

    print(findHeight(BST.root))
