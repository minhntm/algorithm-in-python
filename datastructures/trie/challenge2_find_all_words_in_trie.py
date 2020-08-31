"""
Problem Statement:
- You have to implement the find_words() function which will return a sorted
    list of all the words stored in a trie.

Input:
- The root node of a trie.
Output:
- A sorted list of all the words stored in a trie.
"""


from Trie import Trie


# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
# get_root => trie.get_root()
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)
def find_words(root):
    return list(find(root, ''))


def find(root, path):
    path += root.char
    if root.is_end_word:
        yield path

    for child in root.children:
        if child:
            yield from find(child, path)


if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    t = Trie()
    for i in range(len(keys)):
        t.insert(keys[i])
    lst = find_words(t.root)
    print(str(lst))
