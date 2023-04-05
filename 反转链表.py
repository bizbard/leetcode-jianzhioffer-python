from typing import List

class ListNode:
    """Definition for a singly-linked list node
    """    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    """Generate a linked list with a list

    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """    
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = head.next
    return dum.next

def linked_list_to_list(head):
    """Serialize a linked list into an array

    Args:
        head ([type]): [description]

    Returns:
        [type]: [description]
    """    
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


if __name__ == '__main__':
    # ======= Test Case =======
    head = [1, 2, 3, 4, 5]
    # ====== Driver Code ======
    sol = Solution()
    head = list_to_linked_list(head)
    res = sol.reverseList(head)
    res = linked_list_to_list(res)
    print(res)