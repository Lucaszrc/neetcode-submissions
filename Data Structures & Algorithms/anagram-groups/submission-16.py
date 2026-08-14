from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            results[tuple(sorted(s))].append(s)
        return list(results.values())