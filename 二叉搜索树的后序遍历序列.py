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
    def verifyPostorder(self, postorder: List[int]) -> bool:
        
        def cur(i, j):
            if i >= j: return True
            while postorder[i] <= postorder[j]:
                i += 1
            m = i
            for k in range(i, j):
                if postorder[k] < postorder[j]:
                    return False

            return cur(i, m-1) and cur(m, j-1)

        return cur(0, len(postorder)-1)


if __name__ == '__main__':
    # ======= Test Case =======
    root = [1,3,2,6,5]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.verifyPostorder(root)
    print(res)