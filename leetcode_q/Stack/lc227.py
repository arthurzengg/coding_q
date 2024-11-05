class Solution:
    """
    解题思路：
    1. 使用栈来处理基本的加减乘除运算。栈用于存储数字，当遇到运算符时，根据前一个运算符决定如何处理栈顶的数字。
    2. 遍历字符串，先处理空格的移除。之后，依次处理每个字符，若是数字则可能需要继续向后查找以获取完整的多位数。
    3. 加减运算简单处理，数字直接入栈；乘除运算则需从栈中取出一个数字与当前数字进行计算后，再将结果入栈。
    4. 最终，遍历完字符串后，栈中存放的数字即为所有待加和的数字。通过对栈中数字求和得到最终结果。
    5. 特别注意，乘除运算需要立即计算，而加减运算可以延后处理，这是因为加减运算符号可以通过正负号直接控制数字。

    这种处理方式可以直接利用栈的后进先出特性来逆序处理运算的优先级，适用于没有括号的平面算术表达式。
    """
    def calculate(self, s: str) -> int:
        # 移除空格并初始化变量
        s = s.replace(" ", "")  # 移除字符串中所有的空格
        stack = []  # 使用栈来处理中间结果
        n = len(s)  # 表达式的长度
        sign = '+'  # 初始化符号为加号
        i = 0  # 用索引i来遍历字符串

        while i < n:  # 遍历整个字符串
            num = ''
            if s[i].isdigit():  # 当前字符为数字
                num = s[i]  # 开始记录数字
                while i + 1 < n and s[i + 1].isdigit():  # 处理多位数的情况
                    num = num + s[i + 1]
                    i += 1
                num = int(num)  # 将连续的数字字符转换为整数
                if sign == '+':  # 如果前一个运算符是加号
                    stack.append(num)  # 则将数字直接入栈
                else:  # 如果前一个运算符是减号
                    stack.append(-num)  # 则将数字的相反数入栈
                i += 1
            elif s[i] == '+':  # 遇到加号
                sign = '+'  # 更新运算符
                i += 1
            elif s[i] == '-':  # 遇到减号
                sign = '-'  # 更新运算符
                i += 1
            elif s[i] == '*':  # 遇到乘号
                while i + 1 < n and s[i + 1].isdigit():  # 获取乘号后的完整数字
                    num = num + s[i + 1]
                    i += 1
                num = int(num)
                num_mul = stack.pop()  # 从栈顶取出最近的数字
                stack.append(num_mul * num)  # 计算乘积后重新入栈
                i += 1
            elif s[i] == '/':  # 遇到除号
                while i + 1 < n and s[i + 1].isdigit():  # 获取除号后的完整数字
                    num = num + s[i + 1]
                    i += 1
                num = int(num)
                num_div = stack.pop()  # 从栈顶取出最近的数字
                stack.append(int(num_div / num))  # 计算商后重新入栈，注意整除
                i += 1
            else:
                i += 1  # 其他字符，理论上不会出现，继续遍历

        return sum(stack)  # 将栈中所有的数字求和得到最终的计算结果