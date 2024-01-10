# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
# Output: [1,1,4,2,1,1,0,0]