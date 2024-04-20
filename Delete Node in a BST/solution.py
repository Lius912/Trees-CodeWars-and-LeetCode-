# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return root
        q = deque([root])
        prev_q = deque([None])
        while q:
            cur_node = q.popleft()
            prev_node = prev_q.popleft()
            if cur_node.val == key:
                break
            if cur_node.left:
                q.append(cur_node.left)
                prev_q.append(cur_node)
            if cur_node.right:
                q.append(cur_node.right)
                prev_q.append(cur_node)
        else:
            return root
        print(cur_node.val)
        print(prev_node)
        replacing_node = None
        before_replacing_node = cur_node
        if cur_node.left:
            replacing_node = cur_node.left
            while replacing_node.right:
                before_replacing_node = replacing_node
                replacing_node = replacing_node.right
        elif cur_node.right:
            replacing_node = cur_node.right
            while replacing_node.left:
                before_replacing_node = replacing_node
                replacing_node = replacing_node.left
        print(before_replacing_node)
        if not replacing_node:
            if not prev_node:
                return None
            if cur_node is prev_node.left:
                prev_node.left = None
            else:
                prev_node.right = None
        else:
            if replacing_node is before_replacing_node.left:
                if before_replacing_node is cur_node:
                    before_replacing_node.left = replacing_node.left
                else:
                    before_replacing_node.left = replacing_node.right
            else:
                if before_replacing_node is cur_node:
                    before_replacing_node.right = replacing_node.right
                else:
                    before_replacing_node.right = replacing_node.left
            cur_node.val = replacing_node.val
        return root
        