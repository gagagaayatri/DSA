# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      return len(nums)!=len(set(nums))

## A set cannot have duplicates, so I found this to be the easiest way to check if there are duplicates or not. If there are duplicates, then the length of the array and length of set won't match :3
      
      


