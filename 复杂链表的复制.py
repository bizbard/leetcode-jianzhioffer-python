from typing import List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return 
        dic = {}

        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head

        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]


if __name__ == '__main__':
    # ======= Test Case =======
    head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    # ====== Driver Code ======
    sol = Solution()