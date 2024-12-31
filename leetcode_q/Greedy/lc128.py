class Solution:
    """
    思路：
    1. 首先，将数组转换为集合，目的是去除重复元素，并且在后续操作中检查元素是否存在可以达到 O(1) 的时间复杂度。
    2. 遍历集合中的每个元素，针对每个元素检查其是否可能是连续序列的起始点，即检查 num-1 是否不在集合中。
       - 如果 num-1 不在集合中，说明 num 可能是一个新的连续序列的起始点。
    3. 从 num 开始，尝试逐个检查 num+1, num+2, ..., 是否存在于集合中，直到找不到连续的数字，统计这一过程中的长度。
    4. 更新并记录遇到的最长的连续序列长度。
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1

                while num + length in nums:
                    length += 1

                max_len = max(max_len, length)

        return max_len