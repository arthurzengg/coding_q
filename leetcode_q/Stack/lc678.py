class Solution:
    """
    解法：
    - 使用两个栈，一个存放左括号 '(' 的索引，另一个存放星号 '*' 的索引。
    - 在遍历过程中：
        - 每遇到 '(' 就入左括号栈。
        - 每遇到 '*' 就入星号栈。
        - 每遇到 ')' 时，优先尝试匹配 '('，没有就尝试匹配 '*'。
        - 若两者都无法匹配，则字符串非法，返回 False。

    - 遍历完后，可能还存在多余的 '(' 和 '*'。
        - 我们希望每一个 '(' 后面都能有一个 '*' 作为 ')'
        - 所以我们从后往前尝试一一匹配 '(' 和 '*'，要求 '*' 的索引必须大于 '(' 的索引。
        - 如果出现 '(' 的位置在 '*' 之后，就无法匹配，返回 False。

    - 如果最终 '(' 栈清空，表示匹配成功，返回 True。
    """

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        star_stack = []
        left_bracket_stack = []
        for i in range(n):
            if s[i] == "(":
                left_bracket_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if left_bracket_stack:
                    left_bracket_stack.pop(-1)
                elif star_stack:
                    star_stack.pop(-1)
                else:
                    return False

        while left_bracket_stack and star_stack:
            if left_bracket_stack[-1] < star_stack[-1]:
                left_bracket_stack.pop(-1)
                star_stack.pop(-1)
            else:
                return False

        return not left_bracket_stack