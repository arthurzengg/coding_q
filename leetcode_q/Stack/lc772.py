class Solution:
    """
    # 思路：
    1. 使用栈（stack）来处理操作符前后的数值运算。
    2. 使用变量operator来记录当前操作符，初始为'+'。
    3. 遍历字符串s，使用变量num来累计数字，当遇到操作符或括号时处理之前的数字和操作符。
    4. 如果遇到'('，则找到对应的')'，递归计算括号内的表达式结果，并将结果作为当前的num。
    5. 根据操作符将num入栈，注意乘除法需要立即计算，加减法则直接入栈。
    6. 遍历完成后，栈内的所有数字相加即为最终结果。
    """


def calculate(self, s: str) -> int:
    n = len(s)
    stack = []
    operator = '+'
    num = 0
    i = 0

    while i < n:
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] == '(':
            j = i + 1
            count = 1
            while j < n:
                if s[j] == '(':
                    count += 1
                elif s[j] == ')':
                    count -= 1
                    if count == 0:
                        break
                j += 1

            num = self.calculate(s[i + 1:j])
            i = j

        if i == n - 1 or s[i] in '+-*/':
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            operator = s[i]
        i += 1
        print(stack)
    return sum(stack)


```