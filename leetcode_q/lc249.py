from collections import defaultdict
class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        string_dict = defaultdict(list)  # 使用defaultdict来存储具有相同模式的字符串

        for string in strings:
            index_compare = []  # 用于存储当前字符串的字符间相对距离
            for c in string:
                # 计算每个字符与第一个字符的相对距离，并处理负数情况
                distance = (ord(string[0]) - ord(c)) % 26
                index_compare.append(distance)

            # 将具有相同相对距离模式的字符串分组
            string_dict[tuple(index_compare)].append(string)

        # 返回分组后的字符串列表
        return string_dict.values()

sol = Solution()
print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
# Output: dict_values([['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']])