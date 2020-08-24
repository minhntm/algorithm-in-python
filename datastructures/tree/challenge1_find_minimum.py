def findMin(root):
    if not root:
        return None
    if root.leftChild:
        return findMin(root.leftChild)
    return root.val
