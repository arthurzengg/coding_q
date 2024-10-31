


# 和leetcode 159的思路是一样的

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}

        n = len(s)
        left, right = 0, 0
        res = 0
        for i in range(n):
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) > k:
                min_value_index = min(hashmap.values())
                hashmap.pop(s[min_value_index])
                left = min_value_index + 1
            res = max(res, right - left)
        return res
