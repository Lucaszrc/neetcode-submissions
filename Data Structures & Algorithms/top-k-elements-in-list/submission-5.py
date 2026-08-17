class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} # frequency : number
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        sorted_nums = sorted(hashMap.keys(), key=lambda x: hashMap[x], reverse=True)
        return sorted_nums[:k]
            
