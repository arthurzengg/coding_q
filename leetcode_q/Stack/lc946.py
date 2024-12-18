class Solution:
    """
    此解法用于验证给定的推入和弹出序列是否可能表示同一个栈的操作序列。
    思路：
    1. 使用一个辅助栈来模拟推入和弹出操作。
    2. 遍历推入序列，每次将元素推入辅助栈。
    3. 在每次推入操作后，检查辅助栈的栈顶元素是否与弹出序列的当前首元素相同。
       - 如果相同，则从辅助栈中弹出该元素，并从弹出序列中移除该首元素。
       - 这个过程可能连续发生，即连续弹出辅助栈的栈顶元素，同时连续移除弹出序列的首元素。
    4. 在所有推入操作完成后，如果辅助栈为空，则意味着弹出序列可以完全通过一系列的推入和弹出操作来实现。

    方法：
    - validateStackSequences(pushed, popped): 输入推入序列 pushed 和弹出序列 popped，返回一个布尔值表示是否可能实现。
    """

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
        return stack == []