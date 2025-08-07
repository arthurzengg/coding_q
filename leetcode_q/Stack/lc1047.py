class Solution:
    """
    解题思路如下：
    1. 使用栈结构来模拟字符的“相邻抵消”过程。
    2. 从左到右遍历字符串：
        - 如果当前字符和栈顶字符相同，则表示形成一对，应当抵消，执行 `pop`；
        - 否则，将当前字符入栈。
    3. 最终栈中留下的字符顺序即为删除所有相邻重复对后的结果。
    4. 返回 `"".join(stack)` 即可得到最终字符串。

    时间复杂度：O(n)，只遍历了一遍字符串；
    空间复杂度：O(n)，最坏情况下所有字符都入栈。
    """

    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if stack and stack[-1] == s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
        return "".join(stack)