from collections import Counter
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        res = []
        count_list = [(-v, c) for c, v in Counter(s).items()]
        heapq.heapify(count_list)
        q = deque()
        while count_list:
            v, c = heappop(count_list)
            v *= -1
            res.append(c)
            q.append((v - 1, c))
            if len(q) >= k:
                v, c = q.popleft()
                if v:
                    heappush(count_list, (-v, c))
        print(res)
        if len(res) != len(s):
            return ''
        else:
            return ''.join(res)