class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        计算字符串 s 中长度为 k 的不含重复字符的子串数量。
        方法使用滑动窗口和哈希表来跟踪字符最后一次出现的位置。
        滑动窗口通过右指针 right 来扩展，并在发现重复字符时适当地调整窗口大小。

        参数:
        s: 输入的字符串
        k: 子串的目标长度

        返回:
        不含重复字符的长度为 k 的子串的数量。
        """
        n = len(s)
        if k > n:
            return 0

        ans = 0
        hashmap = {}
        for right in range(n):

            # 当前字符如果已经在哈希表中，并且之前的位置在考虑的范围内，则移除所有在该位置之前的字符
            if s[right] in hashmap:
                char_remove = []
                for i in hashmap.values():
                    if i < hashmap[s[right]]:
                        char_remove.append(i)
                for i in char_remove:
                    del hashmap[s[i]]  # 这里应该用 s[i] 来删除，而不是直接 i

            # 更新当前字符的位置
            hashmap[s[right]] = right

            # 如果哈希表的大小超过 k，删除最早的字符以保持窗口大小为 k
            if len(hashmap) > k:
                min_index = min(hashmap.values())
                hashmap.pop(s[min_index])

            # 如果窗口大小正好为 k，计数增加
            if len(hashmap) == k:
                ans += 1

        return ans