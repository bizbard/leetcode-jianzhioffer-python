from typing import List
import math


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()
        return num

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    # ======= Test Case =======
    minStack = MinStack()
    # ====== Driver Code ======
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.min()
    minStack.pop()
    minStack.top()
    minStack.min()