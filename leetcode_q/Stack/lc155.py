class MinStack:
    """
    解析：
    1. 栈中可以append(val, cur_min) 去记录当前最小值，如果栈没有元素，cur_min等于val
    2. 如果val < cur_mini，append((val, cur_mini))
    """

    def __init__(self):
        self.miniStack = []

    def push(self, val: int) -> None:
        if not self.miniStack:
            self.miniStack.append((val, val))
        else:
            cur_mini = self.miniStack[-1][1]
            if cur_mini < val:
                self.miniStack.append((val, cur_mini))
            else:
                self.miniStack.append((val, val))

    def pop(self) -> None:
        self.miniStack.pop()

    def top(self) -> int:
        return self.miniStack[-1][0]

    def getMin(self) -> int:
        return self.miniStack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()