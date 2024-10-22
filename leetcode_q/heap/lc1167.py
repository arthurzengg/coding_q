import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            a, b = heapq.heappop(sticks), heapq.heappop(sticks)
            res += a + b
            heapq.heappush(sticks, a + b)
        return res



# 手撕heap
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        # 添加新元素到堆的末尾
        self.heap.append(val)
        # 执行上浮操作
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        # 将最后一个元素移到顶部
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # 执行下沉操作
        if self.heap:
            self.heapify_down(0)
        return root_value

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        child_index = 2 * index + 1  # 左孩子的索引
        while child_index < len(self.heap):
            # 找到最小的孩子
            right_child_index = child_index + 1
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[child_index]:
                child_index = right_child_index
            # 如果父节点大于最小孩子，则交换
            if self.heap[index] > self.heap[child_index]:
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                index = child_index
                child_index = 2 * index + 1
            else:
                break


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = MinHeap()
        for stick in sticks:
            heap.push(stick)

        res = 0
        while len(heap.heap) > 1:
            a = heap.pop()
            b = heap.pop()
            res += a + b
            heap.push(a + b)
        return res