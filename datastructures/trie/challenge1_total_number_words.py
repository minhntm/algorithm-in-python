"""
Problem Statement:
- Implement the total_words() function which will find the total number
    of words in a trie.

Input:
- The root node of a trie.
Output:
- Returns total number of words in a trie.
"""


from Trie import Trie
from collections import deque


# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
def total_words(root):
    q = deque()
    q.append(root)
    word_number = 0

    while len(q):
        current_node = q.popleft()
        if current_node.is_end_word:
            word_number += 1
        for child in current_node.children:
            if child:
                q.append(child)

    return word_number


if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    trie = Trie()

    for key in keys:
        trie.insert(key)

    print(total_words(trie.root))
