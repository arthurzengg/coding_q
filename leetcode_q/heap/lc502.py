import heapq


class Solution:
    """
    1. 将初始资本设为 w，所有项目的资本和利润组成一个列表，每个项目表示为 (capital, profit)。
    2. 首先将项目按所需资本排序，以便从最小的资本要求开始考虑。
    3. 使用最大堆（优先队列）来存储当前可以投资的项目的利润，堆中的元素为负值以模拟最大堆的效果。
    4. 进行最多 k 轮投资：
       - 遍历所有项目，将所有当前资本 w 能够投资的项目的利润加入到堆中。
       - 如果堆不为空，则从堆中弹出最大利润，更新当前资本 w。
       - 如果当前资本不足以投资任何剩余项目且堆为空，则终止循环。
    5. 循环结束后，当前的资本 w 就是最大化后的资本。

    关键点：
    - 排序确保我们总是首先考虑最小资本要求的项目。
    - 堆用来快速获得当前可投资的项目中利润最大的项目。
    - 每次投资都可能使得新的项目变得可行，因此需要动态更新可投资的项目列表。
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        combine_information = []
        res = w
        for i in range(n):
            combine_information.append((capital[i], profits[i]))

        combine_information.sort(key=lambda x: x[0])
        if combine_information[0][0] > w:
            return res

        heap = []
        heapq.heapify(heap)
        while k > 0:
            while combine_information:
                c = combine_information[0][0]
                p = combine_information[0][1]
                if res >= c:
                    c, p = combine_information.pop(0)
                    heapq.heappush(heap, -p)
                else:
                    break
            if heap:
                max_profit = -heapq.heappop(heap)
                res += max_profit
            k -= 1
        return res

