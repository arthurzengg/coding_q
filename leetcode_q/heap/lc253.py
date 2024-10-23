import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        # 按照会议的开始时间排序
        intervals.sort(key=lambda x: x[0])

        # 创建一个最小堆，用来维护会议的结束时间
        heap = []

        # 遍历排序后的会议时间
        for interval in intervals:
            if heap and interval[0] >= heap[0]:
                # 如果当前会议的开始时间大于等于堆顶的会议结束时间
                # 弹出堆顶，即旧的结束时间，并将新的结束时间压入堆中
                heapq.heappop(heap)
            # 将当前会议的结束时间加入到堆中
            heapq.heappush(heap, interval[1])

        # 堆的大小就是所需的会议室数量
        return len(heap)


# 示例测试
sol = Solution()
print(sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 输出 2
print(sol.minMeetingRooms([[7, 10], [2, 4]]))  # 输出 1