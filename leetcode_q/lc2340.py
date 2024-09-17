class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == max_num:
                max_index = i
                break
        for j in range(n):
            if nums[j] == min_num:
                min_index = j
                break

        if max_index > min_index:
            return n - max_index + min_index - 1
        else:
            return n - max_index + min_index - 2
