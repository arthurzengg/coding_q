class Solution:
    """
    思路：
    1. 首先将勒索信字符串和杂志字符串转换为列表并排序。排序是为了让相同的字符彼此靠近，方便后续比较。
    2. 使用两个指针 i 和 j 分别指向 ransomNote 和 magazine 的起始位置。
    3. 遍历这两个已排序的列表：
       - 如果两个指针指向的字符相同，说明当前字符可以从杂志中拿来用在勒索信上，两个指针都向前移动。
       - 如果不同，说明杂志中的当前字符无法用于勒索信，只移动杂志的指针 j。
    4. 如果 ransomNote 中的所有字符都能在 magazine 中找到匹配，则返回 True。
    5. 遍历结束后，如果 ransomNote 有未被匹配的字符，返回 False。
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        ransomNote.sort()
        magazine.sort()

        i = 0
        j = 0
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(ransomNote)


"""
HashMap
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Create a dictionary to store character counts
        dictionary = {}

        # Iterate through the magazine and count characters
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        # Iterate through the ransom note and check character counts
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False

        return True