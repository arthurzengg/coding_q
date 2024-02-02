class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_num = 0
        operators = {'+', '-', '*', '/'}
        operator = '+'
        for index, char in enumerate(s):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            if index == len(s) - 1 or char in operators:
                if operator == '+':
                    stack.append(cur_num)
                elif operator == '-':
                    stack.append(-cur_num)
                elif operator == '*':
                    num_front = stack.pop(-1)
                    cur_num = cur_num * num_front
                    stack.append(cur_num)
                elif operator == '/':
                    num_front = stack.pop(-1)
                    if num_front < 0:
                        cur_num = abs(num_front) // cur_num
                        stack.append(-cur_num)
                    else:
                        stack.append(num_front // cur_num)

                cur_num = 0
                operator = char

        return sum(stack)


sol = Solution()
print(sol.calculate("3-2*2"))
# Output: -1