class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = []

        def heapify(root, n, i):
            """
            i: 当前需要“向下调整”（sift down）的节点下标
            n: 当前堆的有效大小
            root: 存储数据的列表（在此就是nums）
            """
            max_node = i
            left_child = i * 2 + 1
            right_child = i * 2 + 2
            # 找到左右孩子里比自己更大的节点
            if left_child < n and root[i] < root[left_child]:
                max_node = left_child
            if right_child < n and root[max_node] < root[right_child]:
                max_node = right_child

            # 如果最大的不是自己，说明需要和子节点交换，并继续向下调整
            if root[max_node] != root[i]:
                root[i], root[max_node] = root[max_node], nums[i]
                """
                换完以后，原本的父节点就被移到子节点位置上，这个子节点下面可能还有子孙节点；
                因此，我们必须继续在新的位置进行检查和交换，以保证整个子树依然符合大顶堆的性质。
                """
                heapify(root, n, max_node)

        def heap_sort(root, n):
            for i in range((n - 1 - 1) // 2, -1, -1):
                heapify(root, n, i)

        # 1. 一次性建堆（大顶堆）
        n = len(nums)
        heap_sort(nums, n)

        # 2. 取出堆顶 k 次
        while k > 0:
            # 把堆顶（当前最大）和堆尾互换
            nums[0], nums[-1] = nums[-1], nums[0]
            # 弹出堆顶
            top = nums.pop()  # 这个就是本轮最大值
            sorted_nums.append(top)
            n = len(nums)
            if n == 0:
                break
            # 只需对新的根节点做一次heapify（向下调整）
            heapify(nums, n, 0)
            k -= 1

        # 第 k 大元素即为最后一次弹出的top
        return top