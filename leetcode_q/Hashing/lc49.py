from collections import defaultdict


class Solution:
    """
    思路：
    1. 创建一个默认字典 hashmap，其键是排序后的字符串，值是一个列表，用来存储所有匹配该排序键的原字符串。
    2. 遍历字符串数组 strs 中的每个字符串：
       - 将每个字符串按字符排序（转换为列表后排序，再转回字符串），得到排序后的字符串作为键。
       - 将原字符串添加到对应键的列表中。
    3. 遍历 hashmap，将每个键对应的列表收集到结果列表 res 中。
       - 这样，每个列表都包含了一组互为字母异位词的字符串。

    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)
        for word in strs:
            hashmap[str(sorted(word))].append(word)
        for key, value in hashmap.items():
            res.append(value)
        return res
