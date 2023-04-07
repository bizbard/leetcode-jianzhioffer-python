from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        new_headA = headA
        new_headB = headB

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
            if not headA and headB:
                headA = new_headB

            if not headB and headA:
                headB = new_headA

            if not headA and not headB:
                return None


if __name__ == '__main__':
    # ======= Test Case =======
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,0,1,8,4,5]
    skipA = 2
    skipB = 3
    # ====== Driver Code ======
    sol = Solution()
    res = sol.getIntersectionNode(listA, listB)
    print(res)