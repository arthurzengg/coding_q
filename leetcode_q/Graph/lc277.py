# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    """
    # 思路：
    1. 假设第一个人（编号为 0）是名人候选人。
    2. 遍历从 1 到 n-1 的所有人，判断当前候选人是否认识第 i 个人：
       - 如果候选人认识 i，则候选人不可能是名人，将候选人更新为 i。
       - 如果候选人不认识 i，则继续保持当前候选人。
    3. 完成第一轮遍历后，得到一个名人候选人，需要验证其是否真正是名人。
    4. 验证步骤：
       - 再次遍历所有人，检查以下两点：
         a. 候选人不应认识任何其他人（除了自己）。
         b. 其他所有人都应认识候选人。
       - 如果上述任一条件不满足，则返回 -1，表示不存在名人。
    5. 如果候选人通过了验证，返回候选人的编号。
    """

    def findCelebrity(self, n: int) -> int:
        possible = 0
        for i in range(1, n):
            if knows(possible, i):
                possible = i

        for i in range(n):
            if i == possible:
                continue
            if knows(possible, i) or not knows(i, possible):
                return -1
        return possible