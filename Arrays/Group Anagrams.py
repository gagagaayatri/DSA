'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagramMap = defaultdict(list) 
      for word in strs:
        sorted_word = ''.join(sorted(word)) #sort the word 
        anagramMap[sorted_word].append(word) #use the word as the key, if its an anagram the key would be same and word will be appended to that.
      return list(anagramMap.values())
      
