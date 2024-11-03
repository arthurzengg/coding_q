class Solution:
    """
    解题思路：
    1. 创建一个哈希表来存储每个字符在键盘上的位置。
    2. 遍历给定单词的每个字符，计算从上一个字符到当前字符的移动距离，并累加到总时间上。
    3. 初始位置设为第一个字符的位置，这样可以从第一个字符开始计算移动距离。
    4. 返回计算的总移动时间。

    此解法的时间复杂度为O(N)，其中N是word的长度，因为我们只需要遍历一次单词即可完成所有计算。
    空间复杂度为O(1)，因为哈希表的大小固定为键盘字符的数量，与单词长度无关。
    """

    def calculateTime(self, keyboard: str, word: str) -> int:
        n = len(keyboard)
        hashmap = {}
        for i in range(n):
            hashmap[keyboard[i]] = i

        ans = 0

        last_index = 0
        for char in word:
            ans += abs(hashmap[char] - last_index)
            last_index = hashmap[char]

        return ans