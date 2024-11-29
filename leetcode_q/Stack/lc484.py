class Solution:
    """
    此解法用于根据给定的规则字符串s找出满足条件的整数序列。
    思路：
    1. 根据字符串s的长度n初始化一个从1到n+1的整数序列res。
    2. 遍历字符串s，使用贪心算法根据字符'D'（降序）和'I'（升序）调整序列。
    3. 对于每个字符，如果是'D'，则寻找连续的'D'并将对应的序列部分进行反转以形成降序；如果是'I'，则继续遍历。
    4. 最终返回调整后的序列res，该序列根据s中的规则正确地表示了数字间的顺序关系。

    方法：
    - findPermutation(self, s: str) -> List[int]: 主函数，遍历字符串并根据字符调整序列。
    """
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        res = [i for i in range(1, n + 2)]
        i = 0

        while i < n:
            if s[i] == 'D':
                right = i
                while right < n and s[right] == 'D':
                    right += 1
                res[i: right + 1] = res[i: right + 1][::-1]
                i = right
            else:
                i += 1

        return res


class Solution:
    """
    此解法使用栈来根据给定的规则字符串s找出满足条件的整数序列。
    思路：
    1. 根据字符串s的长度n初始化一个从1到n+1的整数序列。
    2. 遍历字符串s，对于每个字符，将当前的数字压入栈中。
    3. 当遇到字符'I'或到达字符串的末尾时，从栈中弹出所有元素并添加到结果列表中，这样可以保证序列的递增。
    4. 如果遇到连续的'D'，继续压栈，直到遇到'I'，此时从栈中弹出元素，由于栈的后进先出特性，可以自动形成降序。
    5. 最终返回调整后的序列，该序列根据s中的规则正确地表示了数字间的顺序关系。

    方法：
    - findPermutation(self, s: str) -> List[int]: 主函数，利用栈操作处理数字，生成符合降序和升序规则的序列。
    """

    def findPermutation(self, s: str) -> List[int]:
        # 初始化栈和结果数组
        stack = []
        result = []
        # 根据s的长度加1来确定数字的范围，因为数字从1开始到n+1
        n = len(s) + 1

        for i in range(1, n + 1):
            # 将每个数字压入栈中
            stack.append(i)
            # 当遇到'I'或遍历到最后一个数字时，开始弹栈操作
            if i == n or s[i - 1] == 'I':
                # 栈中元素逆序输出，确保降序和升序规则得到满足
                while stack:
                    result.append(stack.pop())

        return result