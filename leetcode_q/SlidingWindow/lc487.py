class Solution:
    """
    此函数用于在二进制数组`nums`中找到连续1的最大个数。
    它允许翻转最多一个0为1，以最大化连续1的序列。

    思路：
    - 使用两个指针`left`和`right`表示连续1的窗口。
    - 通过移动`right`指针扩展窗口，并在遇到第一个0时翻转为1，并记录其索引。
    - 如果再次遇到0，并且已经进行过一次翻转，就将`left`指针移动到第一个被翻转的0之后的位置，从而开始新的窗口。
    - 持续更新遇到的1的窗口的最大长度。
    - 循环直到`right`指针扫描完整个数组。

    该解决方案有效地管理了窗口以确保找到考虑单次翻转允许的最长1的序列。
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0  # 初始化左右指针
        n = len(nums)  # 数组的长度
        is_flip = False  # 标志是否已经翻转过0
        max_len = 0  # 用来存储找到的最大连续1的长度
        flip_index = -1  # 被翻转0的索引，初始化为-1（表示未进行翻转）

        while right < n:  # 当右指针没有超出数组长度时循环
            if nums[right] == 0 and not is_flip:
                # 如果当前元素是0并且之前没有进行过翻转
                is_flip = True  # 设置翻转标志为真
                flip_index = right  # 记录翻转的位置
            elif nums[right] == 0 and is_flip:
                # 如果再次遇到0且已经翻转过一个0
                left = flip_index + 1  # 将左指针移动到第一个被翻转的0之后的位置
                flip_index = right  # 更新翻转的位置（尽管按照题意只翻转一次，这里更新为了维护逻辑一致性）

            right += 1  # 移动右指针
            # 更新窗口的最大长度
            max_len = max(max_len, right - left)

        return max_len  # 返回最大连续1的长度