"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

The solution will use a bucket sort method. The values of the hashmap would be the index of the table, and the index would become the values.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {} #Initialize empty hashmap
      frequency = [[] for i in range(len(nums)+1)] #Create empty table
      for n in nums:
        count[n]= 1 + count.get(n,0) #Count the frequency of each element
      for n,c in count.items():
        freq[c].append(n) #The frequency would be the index of the table, while the key would be the value.
      #Retrieve in descending order
      res = []
      for i in range(len(freq)-1,0,-1):
        for n in freq[i]: #values for the ith index (i.e the element)
          res.append(n)
          if len(res) == k:
            return res

