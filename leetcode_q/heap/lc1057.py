import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)  # 获取工人的数量
        m = len(bikes)  # 获取自行车的数量
        axis = []  # 创建一个空列表来存储距离和对应的索引

        # 计算每个工人和每辆自行车之间的曼哈顿距离，并将其与索引一起放入优先队列（堆）
        for i in range(n):
            for j in range(m):
                manhattan_dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                heapq.heappush(axis, (manhattan_dis, i, j))

        # 初始化结果数组，所有元素初始值为-1，代表尚未分配自行车
        res = [-1 for _ in range(n)]
        bike_used = set()  # 创建一个集合来记录已经被分配的自行车
        worker_used = set()  # 创建一个集合来记录已经被分配自行车的工人

        # 从堆中取出元素，直到堆为空
        while axis:
            manhattan_dis, worker_id, bike_id = heapq.heappop(axis)
            # 确保当前工人和自行车都未被之前的操作分配
            if worker_id not in worker_used and bike_id not in bike_used:
                res[worker_id] = bike_id  # 为工人分配自行车
                bike_used.add(bike_id)  # 标记自行车为已分配
                worker_used.add(worker_id)  # 标记工人为已分配

        return res  # 返回分配结果