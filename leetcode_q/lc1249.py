class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_list = []
        valid_map = {')':'('}
        for i in range(len(s)):
            if s[i] in valid_map:
                if stack:
                    stack.pop()
                    remove_list.pop()
                else:
                    remove_list.append(i)
            else:
                if s[i] == '(':
                    stack.append(s[i])
                    remove_list.append(i)
        s = list(s)
        for index in remove_list:
            s[index] = ''
        s = ''.join(s)
        return s

sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
# output: lee(t(c)o)de