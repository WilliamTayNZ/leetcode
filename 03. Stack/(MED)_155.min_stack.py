class MinStack:
    def __init__(self):
        self.array = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.minimums:
            if val < self.minimums[-1]:
                self.minimums.append(val)
            else:
                self.minimums.append(self.minimums[-1])
        else:
            self.minimums.append(val)
            # note: you cannot append with index like self.minimums[new_index] = val.
            # Will be index error
        
    def pop(self) -> None:
        self.array.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minimums[-1]    
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# December 2nd, 2025