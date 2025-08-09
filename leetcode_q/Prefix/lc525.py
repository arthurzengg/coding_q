class Solution:
    """
    中文思路解析：
    将 0 视为 -1，1 视为 +1。遍历数组时维护“前缀和”count：
    - 若在两个位置 i、j（i<j）前缀和相同，即 count[i] == count[j]，
      则区间 (i, j] 的元素和为 0，说明该子数组内 0 和 1 数量相同。
    - 用哈希表 first_index 记录“某个前缀和值第一次出现的下标”，
      当再次遇到相同前缀和时，用当前位置减去第一次出现位置即可得到一段和为 0 的最长区间长度。
    细节：
    - 预置 first_index[0] = -1，表示从起点到当前的前缀和为 0 时长度可直接用 i - (-1) = i+1。
    时间复杂度 O(n)，空间复杂度 O(n)。
    """
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0
        hashmap = {0: -1}
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in hashmap:
                res = max(res, i - hashmap[count])
            else:
                hashmap[count] = i
        return res