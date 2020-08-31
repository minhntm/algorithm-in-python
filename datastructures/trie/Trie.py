class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # Total size of the English alphabet
        self.is_end_word = False  # True if the node represents the end of word
        self.char = char  # To store the value of a particular key

    # Function to mark the currentNode as Leaf
    def mark_as_leaf(self):
        self.is_end_word = True

    # Function to unMark the currentNode as Leaf
    def unmark_as_Leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key into the trie
    def insert(self, key):
        # None keys are not allowed
        if key is None:
            return

        key = key.lower()  # Keys are stored in lowercase
        current_node = self.root
        index = 0  # To store the character index

        # Iterate the trie with the given character index,
        # If the index points to None
        # simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])

            current_node = current_node.children[index]

        # Mark the end character as leaf node
        current_node.mark_as_leaf()

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current_node = self.root
        index = 0

        # Iterate the Trie with given character index,
        # If it is None at any point then we stop and return false
        # We will return true only if we reach leafNode and have traversed the
        # Trie based on the length of the key

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node is not None and current_node.is_end_word:
            return True

        return False

    # Helper Function to return true if current_node does not have any children

    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True

    # Recursive function to delete given key
    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if current_node is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # If we have reached at the node
        # which points to the alphabet at the end of the key.
        if level is length:
            # If there are no nodes ahead of this node in this path
            # Then we can delete this node
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True

            # If there are nodes ahead of current_node in this path
            # Then we cannot delete current_node. We simply unmark this as leaf
            else:
                current_node.unMarkAsLeaf()
                deleted_self = False

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            if child_deleted:
                # Making children pointer also None: since child is deleted
                current_node.children[self.get_index(key[level])] = None
                # If current_node is leaf node then
                # current_node is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current_node.is_end_word:
                    deleted_self = False

                # If child_node is deleted and current_node has more children
                # then current_node must be part of another key
                # So, we cannot delete currenNode
                elif self.has_no_children(current_node) is False:
                    deleted_self = False

                # Else we can delete current_node
                else:
                    current_node = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return

        self.delete_helper(key, self.root, len(key), 0)


if __name__ == "__main__":
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    output = ["Not present in trie", "Present in trie"]

    t = Trie()
    print("Keys to insert: ")
    print(keys)

    # Construct Trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    if t.search("the") is True:
        print("the --- " + output[1])
    else:
        print("the --- " + output[1])

    if t.search("these") is True:
        print("these --- " + output[1])
    else:
        print("these --- " + output[0])

    if t.search("abc") is True:
        print("abc --- " + output[1])
    else:
        print("abc --- " + output[1])

    t.delete("abc")
    print("Deleted key \"abc\"")

    if t.search("abc") is True:
        print("abc --- " + output[1])
    else:
        print("abc --- " + output[0])
