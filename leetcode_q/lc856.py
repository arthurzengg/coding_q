class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)  # 获取字符串的长度
        stack = []  # 初始化一个栈
        stack.append(0)  # 在栈中放入一个初始值 0

        for i in range(n):  # 遍历字符串中的每个字符
            # print(stack)  # 打印当前栈的状态，用于调试
            if s[i] == '(':  # 如果当前字符是左括号 '('
                stack.append(0)  # 在栈中放入一个 0，表示一个新的平衡括号组的开始
            else:  # 如果当前字符是右括号 ')'
                temp = stack.pop()  # 弹出栈顶元素，它可能是 0 或者是一个计算过的分数
                if temp == 0:  # 如果弹出的元素为 0
                    stack[-1] += 1  # 说明这是一对 "()”，给前一个栈顶元素加 1
                else:  # 如果弹出的元素不是 0
                    stack[-1] += 2 * temp  # 说明这是一个嵌套的括号，加上 2 倍的内部分数

        return stack[-1]  # 返回栈顶元素，即整个字符串的分数

sol = Solution()
print(sol.scoreOfParentheses("()()"))