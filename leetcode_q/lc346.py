class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.stack = []

    def next(self, val: int) -> float:
        if len(self.stack) >= self.size:
            self.stack.pop(0)
            self.stack.append(val)
            return sum(self.stack) / self.size
        else:
            self.stack.append(val)
            return sum(self.stack) / len(self.stack)

movingAverage =MovingAverage(3);
print(movingAverage.next(1)) # return 1.0 = 1 / 1
print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3