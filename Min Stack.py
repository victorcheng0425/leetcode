class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li = []
        self.size = -1

    def push(self, x: int) -> None:
        self.size += 1
        if self.li:
            self.li.append((x, min(self.li[-1][1], x)))
        else:
            self.li.append([x,x])

    def pop(self) -> None:
        self.li.pop()

    def top(self) -> int:
        return(self.li[-1][0])

    def getMin(self) -> int:
        return self.li[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
