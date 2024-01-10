# https://leetcode.cn/problems/sliding-window-maximum/solutions/2361228/239-hua-dong-chuang-kou-zui-da-zhi-dan-d-u6h0/
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []  # 存储每个窗口的最大值
        stack = []  # 双端队列，用于存储可能成为最大值的元素的索引
        l = r = 0  # 初始化左右指针，分别代表窗口的左右边界
        n = len(nums)  # 数组的长度

        if n == 1 or k == 1:  # 如果数组只有一个元素或k为1，直接返回原数组
            return nums

        while r < len(nums):  # 遍历数组
            while stack and nums[r] > nums[stack[-1]]:  # 若队列不空且当前元素大于队尾元素
                stack.pop()  # 从队尾移除元素，因为它们不可能是最大值
            stack.append(r)  # 将当前元素的索引添加到队列中

            if stack[0] < l:  # 如果队头元素不在滑动窗口内
                stack.pop(0)  # 从队头移除元素

            if r + 1 >= k:  # 当窗口大小达到k时
                result.append(nums[stack[0]])  # 将当前窗口的最大值添加到结果中
                l += 1  # 将窗口左边界向右移动

            r += 1  # 将窗口右边界向右移动

        return result  # 返回所有窗口的最大值列表


sol = Solution()
print(sol.maxSlidingWindow([4,3,-1,-3,5,3,6,7], 3))
# Output: [4, 3, 5, 5, 6, 7]
