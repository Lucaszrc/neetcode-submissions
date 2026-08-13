from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            sorted_str_key = tuple(sorted(s))
            result[sorted_str_key].append(s)
        
        return list(result.values())
        