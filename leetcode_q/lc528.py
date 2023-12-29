import random
class Solution:

    def __init__(self, w: list[int]):
        self.w = w
        self.element_weight = []
        self.index_list = [i for i in range(len(self.w))]
        self.total_weight = sum(self.w)
        for i in range(len(self.w)):
            self.element_weight.append(self.w[i] / self.total_weight)

    def pickIndex(self) -> int:
        return random.choices(self.index_list, self.element_weight, k=1)[0]

# 根据测试用例进行测试
commands = ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
params = [[[1,3]],[],[],[],[],[]]

# 存储实例化对象
obj = None
results = []

for i, command in enumerate(commands):
    if command == "Solution":
        obj = Solution(*params[i])
        results.append(None)
    elif command == "pickIndex":
        results.append(obj.pickIndex())

print(results)