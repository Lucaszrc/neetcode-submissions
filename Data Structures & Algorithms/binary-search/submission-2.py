class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle_index = (l + r) // 2

            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                l = middle_index + 1
            elif nums[middle_index] > target:
                r = middle_index - 1
        return -1
                