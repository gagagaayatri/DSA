"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      count = defaultdict(int)
      ## defaultdict initializes a default dictionary and can be imported from the collections library 
      for x in s:
        count[x]+=1
        #This will store the frequency of all the letters.
      for x in t:
        count[x]-=1
        #This will decrement the frequency of the letters, and if it is an anagram then the frequency would become zero
      for val in count.values():
            if val != 0:
                return False
      return True
