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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def merge(l1, l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

        return merge(l1, l2)


if __name__ == '__main__':
    # ======= Test Case =======
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    # ====== Driver Code ======
    sol = Solution()
    l1 = list_to_linked_list(l1)
    l2 = list_to_linked_list(l2)
    res = sol.mergeTwoLists(l1, l2)
    res = linked_list_to_list(res)
    print(res)