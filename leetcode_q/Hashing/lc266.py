class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_list = Counter(s)
        odd_count = 0
        for count in count_list.values():
            if count % 2 == 1:
                odd_count += 1
        return odd_count <= 1