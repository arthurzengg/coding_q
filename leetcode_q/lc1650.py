# 解析：两个指针同时向前
# 注意点1：temp_p = temp_p.parent
#         temp_q = temp_q.parent
#         这两个应该在if statement之前，这样两个指针才能同时前进
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        temp_p = p
        temp_q = q
        while temp_p != temp_q:
            temp_p = temp_p.parent
            temp_q = temp_q.parent
            if temp_p == None:
                temp_p = q
            if temp_q == None:
                temp_q = p
        return temp_p

