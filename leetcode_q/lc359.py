class Logger:

    def __init__(self):
        self.timesheet = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timesheet:
            if self.timesheet[message] <= timestamp:
                self.timesheet[message] = 10 + timestamp
                return True
            else:
                return False
        else:
            self.timesheet[message] = timestamp + 10
            return True

logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))  # True
print(logger.shouldPrintMessage(2, "bar"))  # True
print(logger.shouldPrintMessage(3, "foo"))  # False, 10 秒内再次打印
print(logger.shouldPrintMessage(11, "foo")) # True, 因为现在是时间戳 11