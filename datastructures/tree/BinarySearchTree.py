from Node import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False

    def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)
