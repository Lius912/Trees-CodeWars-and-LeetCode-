from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    nodes = []
    stck = deque([node])
    while stck:
        cur_node = stck.popleft()
        nodes.append(cur_node.value)
        if cur_node.left:
            stck.append(cur_node.left)
        if cur_node.right:
            stck.append(cur_node.right)
    return nodes