class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 创建一个栈用于存储之前的字符串和重复次数
        cur_str = []  # 当前正在构建的字符串
        cur_num = 0  # 当前读取的数字，表示重复的次数

        for c in s:  # 遍历给定的字符串
            if '0' <= c <= '9':  # 如果字符是数字
                cur_num = cur_num * 10 + int(c)  # 累积数字，考虑到数字可能有多位
            elif c == '[':  # 如果遇到左括号
                stack.append(cur_str)  # 将当前字符串压入栈
                stack.append(cur_num)  # 将当前数字压入栈
                cur_str = []  # 重置当前字符串
                cur_num = 0  # 重置当前数字
            elif c == ']':  # 如果遇到右括号
                num = stack.pop()  # 从栈中弹出数字，表示重复次数
                pre_str = stack.pop()  # 从栈中弹出之前的字符串
                cur_str = pre_str + num * cur_str  # 构建新的字符串：之前的字符串加上当前字符串重复 num 次
            else:  # 如果是普通字符
                cur_str.append(c)  # 将字符添加到当前字符串
            print('cur_str:', cur_str)
            print('stack:', stack)

        return ''.join(cur_str)  # 将列表中的字符连接成字符串并返回

sol = Solution()
print(sol.decodeString("3[a2[c]]"))
# Output: accaccacc

# cur_str: []
# stack: []

# cur_str: []
# stack: [[], 3]

# cur_str: ['a']
# stack: [[], 3]

# cur_str: ['a']
# stack: [[], 3]

# cur_str: []
# stack: [[], 3, ['a'], 2]

# cur_str: ['c']
# stack: [[], 3, ['a'], 2]

# cur_str: ['a', 'c', 'c']
# stack: [[], 3]

# cur_str: ['a', 'c', 'c', 'a', 'c', 'c', 'a', 'c', 'c']
# stack: []
