from collections import Counter


class Solution:
    """
    题意：判断 s2 中是否存在一个子串，恰好是 s1 的某个排列（字符出现次数完全一致，顺序可变）。

    思路（固定长度滑动窗口 + 计数比较）：
    1) 统计 s1 的字符频次 count（Counter）。
    2) 使用一个长度为 len(s1) 的固定滑动窗口在 s2 上从左到右滑动：
       - 对于每个窗口 s2[left : right+1]，用 Counter 统计其字符频次并与 count 比较；
       - 若两者相等，说明该窗口是 s1 的某个排列，返回 True。
    3) 若所有窗口都不匹配，返回 False。

    复杂度：
    - 每次窗口都重建 Counter，单次 O(|s1|)，窗口数约 O(|s2|)，整体最坏 O(|s1| * |s2|)。
      （可优化为维护窗口计数：进入一个字符 +1、移出一个字符 -1，比较两个 Counter 是否相等，从而将整体降为 O(|s1| + |s2|)。）
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        n = len(s1)
        left = 0
        right = n - 1
        if n > len(s2):
            return False
        while right < len(s2):
            if Counter(s2[left:right + 1]) == count:
                return True
            left += 1
            right += 1
        return False

