from typing import List
import collections
import copy


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
    def treeToDoublyList(self, root: TreeNode):
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)

            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)


        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


if __name__ == '__main__':
    # ======= Test Case =======
    root = [4, 2, 5, 1, 3]
    # ====== Driver Code ======
    sol = Solution()
    res = sol.treeToDoublyList(root)