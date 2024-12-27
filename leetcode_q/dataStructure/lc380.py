import random


class RandomizedSet:
    """
    内部结构：
    - nums：一个列表，用于存储集合中的元素。
    - val_to_index：一个字典，键为元素值，值为该元素在 nums 列表中的索引。

    实现细节：
    - insert 操作：将新元素添加到 nums 列表的末尾，并在 val_to_index 中记录其索引。
    - remove 操作：为了保持 O(1) 的时间复杂度，将要删除的元素与 nums 列表最后一个元素交换位置，
      然后更新 val_to_index，最后从 nums 中移除最后一个元素并更新 val_to_index。
    - getRandom 操作：使用 random.choice() 函数从 nums 中随机选择一个元素返回。
    """

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        else:
            self.val_to_index[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        else:
            remove_index = self.val_to_index[val]
            last_num = self.nums[-1]

            self.nums[remove_index] = last_num
            self.val_to_index[last_num] = remove_index

            self.nums.pop()
            del self.val_to_index[val]

            return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

