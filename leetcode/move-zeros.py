"""
Given an array nums, write a function to move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.

Example:
- Input: [0,1,0,3,12]
- Output: [1,3,12,0,0]

Note:
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.
"""


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    anchor = 0
    explorer = 0
    while explorer < len(nums):
        if nums[explorer] != 0:
            nums[anchor] = nums[explorer]
            anchor = anchor + 1
            
        explorer = explorer + 1
            
    while anchor < len(nums):
        nums[anchor] = 0
        anchor = anchor + 1
