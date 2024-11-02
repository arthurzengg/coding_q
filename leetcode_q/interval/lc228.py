class Solution:
    """
    思路解析：
    这个函数用于将一个整数数组中的连续区间整理成一个字符串列表。具体步骤如下：
    1. 判断数组是否为空，如果为空，则直接返回空列表。
    2. 使用两个指针left和right来遍历数组，left指向当前连续区间的开始位置，right用来探索连续区间的结束位置。
    3. 遍历数组，如果nums[right]与nums[right - 1]连续（即nums[right] == nums[right - 1] + 1），则right指针继续向右移动。
    4. 如果不连续，根据left和right的位置关系，判断是单个元素还是一个范围，然后添加到结果列表中。
    5. 当遍历完成后，需要添加最后一个区间到结果列表中。
    6. 返回结果列表。
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ans = []
        left = 0
        right = 1
        while right < n:
            if nums[right] == nums[right - 1] + 1:
                right += 1
            else:
                if right - left == 1:
                    ans.append(str(nums[left]))
                else:
                    ans.append(f"{nums[left]}->{nums[right - 1]}")
                left = right
                right += 1
        # 处理最后一个区间
        if right - left == 1:
            ans.append(str(nums[left]))
        else:
            ans.append(f"{nums[left]}->{nums[right - 1]}")
        return ans