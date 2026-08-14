from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {} # val : index
        for num in nums:
            if num in prevMap:
                return True
            else:
                prevMap[num] = True
        return False