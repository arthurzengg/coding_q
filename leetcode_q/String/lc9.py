class Solution:
    """
    解法：
    - 首先将整数转为字符串。
    - 然后使用切片反转字符串，比较反转后的结果是否等于原始字符串。
    - 如果相同，说明是回文数，返回 True；否则返回 False。
    """

    def isPalindrome(self, x: int) -> bool:
        x = str(x)              # 将整数转换为字符串
        if x == x[::-1]:        # 字符串反转后和原始字符串对比
            return True
        return False