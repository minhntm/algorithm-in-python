"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
- Input: ["flower","flow","flight"]
- Output: "fl"

Example 2:
- Input: ["dog","racecar","car"]
- Output: ""
- Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ''
    
    for char_index, char in enumerate(strs[0]):
        for i, v in enumerate(strs):
            if len(v) <= char_index or v[char_index] != char:
                return v[:char_index]
    
    return strs[0]
