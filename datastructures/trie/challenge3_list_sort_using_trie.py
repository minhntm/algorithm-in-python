"""
Problem Statement:
- In this problem, you have to implement the sort_list() function
    which will sort the elements of a list of strings.

Input:
- A list of strings.
Output:
- Returns the input list in a sorted state.
"""


from Trie import Trie
# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
# get_root => trie.get_root()
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)


# Recursive Function to generate all words in alphabetic order
def sort_list(arr):
    trie = Trie()
    for s in arr:
        trie.insert(s)
    return list(find(trie.root, ''))

def find(root, path):
    path += root.char
    if root.is_end_word:
        yield path

    for child in root.children:
        if child:
            yield from find(child, path)


if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    print(sort_list(keys))
