from typing import List


class CQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)

    def deleteHead(self) -> int:
        if self.stackB:
            return self.stackB.pop()

        if not self.stackA: return -1

        for i in range(len(self.stackA)):
            num = self.stackA.pop()
            self.stackB.append(num)
        res = self.stackB.pop()
        return res

if __name__ == '__main__':
    # ======= Test Case =======
    obj = CQueue()
    # ====== Driver Code ======
    obj.appendTail(3)
    obj.deleteHead()
    obj.deleteHead()
    obj.deleteHead()