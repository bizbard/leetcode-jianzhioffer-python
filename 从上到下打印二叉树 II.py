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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        cur = [root]

        while cur:
            level = []
            levelval = []
            for node in cur:
                levelval.append(node.val)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            cur = level
            res.append(levelval)

        return res


if __name__ == '__main__':
    # ======= Test Case =======
    root = [3,9,20,None,None,15,7]
    # ====== Driver Code ======
    sol = Solution()
    root = list_to_tree(root)
    res = sol.levelOrder(root)
    print(res)