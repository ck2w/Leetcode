
# bfs-graph
from collections import deque
def bsf_graph(root):
    if not root:
        return
    queue = deque([root])    
    visited = set([root])
    while queue:
        node = queue.popleft()
        # do somethings with the head node or neighbors
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                # do something for neighbor
    return xxx

# dfs-graph
def dfs_graph(root):
    if not root:
        return
    stack = [root]
    visited = set([root])
    while stack:
        node = stack.pop()
        # do somethings with the head node or neighbors
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                # do something for neighbor
    return xxx