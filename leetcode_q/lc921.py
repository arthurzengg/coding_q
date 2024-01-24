class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if p == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    continue
            stack.append(p)
        return len(stack)

sol = Solution()
print(sol.minAddToMakeValid("((("))
# Output: 3