class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = nums.copy()
        for num in nums:
            list1.append(num)
        return list1