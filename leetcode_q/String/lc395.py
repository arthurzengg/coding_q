from collections import Counter
class Solution:
    """
    思路解析：
    1. 先统计字符串中每个字符的频率；
    2. 如果某个字符出现次数小于 k，那么它不可能出现在任何合法子串中；
    就以这个字符为分隔符，把字符串分成若干段，分别递归处理；
    3. 如果所有字符出现次数都 >= k，整个字符串就是符合条件的；
    """

    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        char_count = Counter(s)
        for key, value in char_count.items():
            if value < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(key))
        return n
