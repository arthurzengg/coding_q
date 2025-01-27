class Solution:
    """
    思路解析：

    具体实现方法如下：
    1. 使用最小堆来帮助快速找出当前和最小的数对。
    2. 初始时，从 nums1 中选取前 k 个元素，并将这些元素与 nums2 中的第一个元素组成数对，放入最小堆。
       - 堆中包含三个元素：数对的和，当前数对中来自 nums1 的元素的索引，和来自 nums2 的元素的索引。
    3. 当最小堆不为空且结果列表长度小于 k 时，进行如下操作：
       - 弹出堆顶元素（当前和最小的数对），将其加入结果列表。
       - 检查当前弹出的数对的 nums2 元素的索引是否还有下一个，如果有，将新的数对加入堆中。

    关键点：
    - 使用最小堆可以保证每次弹出的都是当前和最小的数对。
    - 堆的更新确保我们总是考虑到每个元素对应的下一个可能的最小组合。
    - 这种方法特别适用于当两个列表很大，但只需要少量组合时的场景，可以大大减少不必要的计算和存储。
    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 边界情况处理
        if not nums1 or not nums2 or k == 0:
            return []

        # 最小堆 (sum, i, j)
        min_heap = []

        # 1. 初始将 (nums1[i] + nums2[0], i, 0) 全部入堆
        # i 最多只需要到 k-1，因为我们只需要前 k 小的数对
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        res = []
        # 2. 每次从堆中弹出最小的数对，并将对应的 (i, j+1) 入堆
        while min_heap and len(res) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            # 如果 j+1 还在 b 数组范围内，则把 (i, j+1) 入堆
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

        return res