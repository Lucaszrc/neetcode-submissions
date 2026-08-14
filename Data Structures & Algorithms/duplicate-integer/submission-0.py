from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {} # val : index
        i = 0
        for num in nums:
            if num in prevMap:
                return True
            else:
                prevMap[num] = i
                i += 1
        return False