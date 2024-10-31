class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:  # 如果字符串长度小于3，则直接返回其长度
            return n

        # 哈希表用来存储字符和它们最新的索引
        hashmap = {}
        max_len = 1
        left = 0
        right = 0

        for i in range(n):
            hashmap[s[right]] = right
            right += 1

            # 当哈希表大小大于2时，进行缩减
            if len(hashmap) > 2:
                # 找到最小索引
                min_index = min(hashmap.values())
                # 移除最小索引对应的字符
                hashmap.pop(s[min_index])
                # 移动左指针
                left = min_index + 1

            # 更新最大长度
            max_len = max(max_len, right - left)

        return max_len