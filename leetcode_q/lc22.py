class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []  # 用于存储所有合法的括号组合
        path = ''

        # backtracking是一个递归函数，用于生成所有可能的括号组合
        def backtracking(path, left, right):
            # left代表左括号的数量，right代表右括号的数量

            # 如果左括号数量超过n，或者右括号数量超过左括号数量，则返回
            if left > n or right > left:
                return

            # 如果当前路径长度等于n*2，意味着括号组合完成，添加到结果中
            if len(path) == n * 2:
                res.append(path)
                return

            # 尝试添加一个左括号，只要左括号数量不超过n
            backtracking(path + '(', left + 1, right)

            # 尝试添加一个右括号，只要右括号数量不超过左括号数量
            backtracking(path + ')', left, right + 1)

        # 从空路径开始递归
        backtracking(path, 0, 0)
        return res

sol = Solution()
print(sol.generateParenthesis(3))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']