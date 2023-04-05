from typing import List
import collections


class TreeNode:
    """Definition for a binary tree node
    """    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    """Generate a binary tree with a list

    Args:
        arr ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not arr:
        return
    i = 1
    root = TreeNode(int(arr[0]))
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i<len(arr) and arr[i] != None:
            node.left = TreeNode(int(arr[i]))
            queue.append(node.left)
        i += 1
        if i<len(arr) and arr[i] != None:
            node.right = TreeNode(int(arr[i]))
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    """Serialize a tree into an array

    Args:
        root ([type]): [description]

    Returns:
        [type]: [description]
    """    
    if not root: return []
    queue = collections.deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else: res.append(None)
    return res


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def recur(l, r):
            if not l and not r: return True
            if not l or not r or l.val != r.val: return False
            return recur(l.left, r.right) and recur(l.right, r.left)

        return recur(root.left, root.right) if root else True



if __name__ == '__main__':
    # ======= Test Case =======
    root = [1,2,2,3,4,4,3]
    # ====== Driver Code ======
    sol = Solution()
    root = list_to_tree(root)
    res = sol.isSymmetric(root)
    print(res)