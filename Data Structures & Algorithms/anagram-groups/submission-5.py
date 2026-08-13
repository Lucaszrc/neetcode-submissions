from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) 
        # Creates a dictionary where every
        # new key starts with an empty list

        for s in strs: 
            # loop thru every word in the list
            sorted_str_key = tuple(sorted(s))
            # sort the word, store as the key, set as a tuple
            result[sorted_str_key].append(s)
            # add the original word to the group with the same anagram
        
        return list(result.values())
        # returns the list
        