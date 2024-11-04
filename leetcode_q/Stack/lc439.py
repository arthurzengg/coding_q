class Solution:
    """
    解题思路：
    1. 使用栈结构来解析和计算三元表达式。由于三元表达式的计算顺序从右到左，使用栈可以帮助我们按正确的顺序处理元素。
    2. 从字符串的最后一个字符开始遍历，如果遇到的是数字或字符，则直接推入栈中。
    3. 如果遇到的是问号'?'，则说明前面的两个元素是当前条件表达式的两个可能值，前一个字符是条件（T 或 F）。
    4. 根据条件是'T'还是'F'，从栈中弹出两个元素（first 和 second），根据条件选择相应的元素重新压入栈中。
    5. 每处理一次完整的条件表达式后，向左移动两位继续处理，直到遍历完整个表达式字符串。
    6. 最终栈顶的元素即为整个三元表达式的结果。

    这种方法直接使用栈操作来逆序处理表达式，避免了复杂的递归或多次扫描字符串，提高了效率。
    """
    def parseTernary(self, expression: str) -> str:
        n = len(expression)
        stack = []
        i = n - 1

        while i > -1:
            if expression[i] == '?':
                fisrt = stack.pop()
                stack.pop()
                second = stack.pop()
                if expression[i - 1] == 'T':
                    stack.append(fisrt)
                else:
                    stack.append(second)
                i -= 2
            else:
                stack.append(expression[i])
                i -= 1
        return stack[0]