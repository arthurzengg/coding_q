class Solution:
    """
    中文思路解析：
    这个函数用于检查一个整数数组中是否存在一个长度为三的递增子序列。

    具体实现方法如下：
    1. 初始化一个空的列表 stack，用于保存潜在的递增子序列。
    2. 遍历数组 nums：
       - 如果 stack 为空或者当前元素 nums[i] 大于 stack 中的最后一个元素，将 nums[i] 添加到 stack 中。
         - 每次添加元素后，检查 stack 的长度是否为3，如果是，直接返回 True。
       - 如果 nums[i] 小于或等于 stack 的最后一个元素，遍历 stack：
         - 找到第一个大于或等于 nums[i] 的元素并用 nums[i] 替换它，这样做是为了保持 stack 中元素尽可能小，从而有更大的机会找到递增的三元组。（大于等于的作用[1,2,1,2,1,2,1,2,1,2]）
    3. 遍历结束后，如果没有找到长度为三的递增子序列，则返回 False。

    关键点：
    - 列表 stack 用于动态追踪潜在的递增子序列。
    - 通过替换操作，保持 stack 中的每个位置的元素尽可能地小，这样更容易满足递增的条件。
    - 此方法的核心在于用更小的元素更新潜在递增序列的位置，而不是简单地寻找一个固定的三元递增子序列。
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[i] > stack[-1]:
                stack.append(nums[i])
                print(stack)
                if len(stack) == 3:
                    return True
            else:
                for j in range(len(stack)):
                    if nums[i] <= stack[j]:
                        stack[j] = nums[i]
                        break
        return False