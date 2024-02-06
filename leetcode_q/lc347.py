from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter_dict = Counter(nums)
        res = []
        for key, value in counter_dict.most_common():
            res.append(key)
        return res[:k]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
# Output: [1, 2]