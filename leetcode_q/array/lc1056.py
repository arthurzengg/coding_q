class Solution:
    def confusingNumber(self, n: int) -> bool:
        num_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        str_n = str(n)
        rotated = ""

        for char in reversed(str_n):
            if char in num_dict:
                rotated += num_dict[char]
            else:
                return False

        return rotated != str_n

# 用例测试
sol = Solution()
print(sol.confusingNumber(69))  # 应返回True
print(sol.confusingNumber(88))  # 应返回False
print(sol.confusingNumber(962)) # 应返回False，因为2无法翻转