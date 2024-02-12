# 单调栈
class Solution:
    def maximumSwap(self, num: int) -> int:
        # 将数字转换为字符列表，以便于交换
        num = list(str(num))
        n = len(num)
        stack = []  # 用于存储数字中每个位置的索引，以便于找到最大的可交换数

        # 从后向前遍历数字
        for i in range(n - 1, -1, -1):
            # 如果栈为空，或当前数字大于栈顶索引对应的数字，则将当前索引压入栈
            if not stack or num[stack[-1]] < num[i]:
                stack.append(i)

        # 从前向后遍历数字
        for i in range(n):
            # 检查栈是否为空（防止所有数字相同的情况）并且当前索引小于栈顶索引
            if stack and i < stack[-1]:
                # 如果当前数字小于栈顶索引对应的数字，则交换这两个数字
                if num[i] < num[stack[-1]]:
                    num[i], num[stack[-1]] = num[stack[-1]], num[i]
                    break  # 交换后立即退出循环
                else:
                    continue  # 如果当前数字不小于栈顶索引对应的数字，则继续向后查找
            else:
                # 如果当前索引不小于栈顶索引，则从栈中移除栈顶元素
                if stack:
                    stack.pop(-1)

        # 将字符列表转换回整数并返回
        return int(''.join(num))
