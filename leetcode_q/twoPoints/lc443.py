class Solution:
    """
    本题要求我们将字符数组进行原地压缩，如果一个字符连续出现多次，则将字符和出现次数压缩存入原数组中。
    例如：["a","a","b","b","c","c","c"] 被压缩为 ["a","2","b","2","c","3"]，返回长度为 6。

    解题思路如下：
    1. 使用两个指针：一个遍历整个数组（i），一个负责在原地写入压缩后的结果（write_index）。
    2. 用变量 prev_char 记录当前正在统计的字符，char_count 记录该字符出现的次数。
    3. 如果遇到不同的字符，就把上一个字符及其次数写入原数组中：
       - 如果次数为 1，只写字符本身；
       - 如果次数大于 1，则写入字符 + 次数字符串（每一位单独写入）。
    4. 最后一组字符写完遍历后需要手动补写。
    5. 返回 write_index 作为最终数组长度。
    """
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        res = 0
        prev_char = chars[0]
        char_count = 1
        write_index = 0
        for i in range(1, n):
            if chars[i] == prev_char:
                char_count += 1
            else:
                chars[write_index] = prev_char
                write_index += 1
                res += 1
                if char_count > 1:
                    for num in str(char_count):
                        chars[write_index] = num
                        write_index += 1
                        res += 1
                prev_char = chars[i]
                char_count = 1

        chars[write_index] = prev_char
        write_index += 1
        res += 1
        if char_count > 1:
            for num in str(char_count):
                chars[write_index] = num
                write_index += 1
                res += 1

        return res
