class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        不返回任何内容，直接修改 s 列表。
        """

        def reverse(s, start, end):
            """
            辅助函数：用于原地反转 s 中从 start 到 end 的部分。
            """
            while start < end:
                s[start], s[end] = s[end], s[start]  # 交换两个位置的字符
                start += 1  # 前指针向后移
                end -= 1  # 后指针向前移

        # 首先反转整个字符串列表
        reverse(s, 0, len(s) - 1)

        n = len(s)
        start_index = 0  # 初始化单词的起始位置

        # 遍历反转后的字符串列表
        for i in range(n + 1):  # 包含 n 为了处理最后一个单词
            print(i)  # 打印当前的索引值
            if i == n or s[i] == ' ':  # 如果到达字符串末尾或者遇到空格
                reverse(s, start_index, i - 1)  # 反转当前单词
                start_index = i + 1  # 更新下一个单词的起始位置