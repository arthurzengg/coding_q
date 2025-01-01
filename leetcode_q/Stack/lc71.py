class Solution:
    """
    思路：
    1. 首先，使用 '/' 分割输入的路径字符串，得到路径的各个部分。
    2. 使用一个栈来处理路径的各个部分：
       - 如果当前部分是空字符串或者 '.'，则跳过（它们表示当前目录，对路径没有影响）。
       - 如果当前部分是 '..'，则从栈中弹出最上面的元素（表示返回上级目录）。
         但如果栈为空，说明已经在根目录下，无法再返回上级目录，因此忽略此操作。
       - 如果是其他字符串，表示是路径的一个有效部分，将其压入栈中。
    3. 最后，从栈中依次取出所有路径部分，组成最终的简化路径。
       - 如果栈为空，表示路径简化后为根目录，返回 '/'。
       - 否则，将栈中的每个部分用 '/' 连接，构造出简化后的完整路径。
    """

    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        res = ''
        for p in paths:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)

        if not stack:
            return '/'

        for p in stack:
            res += '/' + p
        return res
