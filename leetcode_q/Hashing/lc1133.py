class Solution:
    """
    解题思路：
    1. 首先创建一个哈希表（使用defaultdict），用于统计数组中每个数字的出现次数。
    2. 遍历输入的数字数组，更新哈希表中对应数字的计数。
    3. 创建一个列表用于存储只出现一次的数字。
    4. 遍历哈希表，将出现次数为1的数字添加到列表中。
    5. 如果列表为空，表示没有唯一的数字，返回-1。
    6. 如果列表不为空，返回列表中的最大值。

    这种方法通过哈希表统计次数，然后通过列表找到最大的唯一数字，简单且直接。
    """

    def largestUniqueNumber(self, nums: List[int]) -> int:
        hahsmap = defaultdict(int)
        for num in nums:
            hahsmap[num] += 1
        num_list_one = []
        for num, count in hahsmap.items():
            if count == 1:
                num_list_one.append(num)
        if num_list_one == []:
            return -1
        return max(num_list_one)