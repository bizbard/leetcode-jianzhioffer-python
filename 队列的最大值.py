from typing import List
import collections
import queue


class MaxQueue:

    # def __init__(self):
    #     self.queue = collections.deque()

    # def max_value(self) -> int:
    #     if not self.queue:
    #         return -1
    #     return max(self.queue)

    # def push_back(self, value: int) -> None:
    #     self.queue.append(value)

    # def pop_front(self) -> int:
    #     if not self.queue:
    #         return -1
    #     return self.queue.popleft()

    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self):
        return self.deque[0] if self.deque else -1
    
    def push_back(self, value):
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
    
    def pop_front(self):
        if self.queue.empty():
            return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
        return val

if __name__ == '__main__':
    # ======= Test Case =======
    obj = MaxQueue()
    # ====== Driver Code ======
    param_1 = obj.max_value()
    obj.push_back(1)
    obj.push_back(2)
    param_2 = obj.max_value()
    param_3 = obj.pop_front()
    param_4 = obj.max_value()