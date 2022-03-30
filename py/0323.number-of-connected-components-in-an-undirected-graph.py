#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n       
        
        # use dict to store edges information, easy to find neigbors for a given node
        neighbors_dict = {k: [] for k in range(n)}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            neighbors_dict[node1].append(node2)
            neighbors_dict[node2].append(node1)
        
        visited = set()        
        count = 0
        
        for node in range(n):
            # check if curr node is in new component
            if node not in visited:
                count += 1
            else:
                continue
            
            # new component: notate all connected nodes to visited
            # dfs
            stack = [node]
            while stack:
                curr_node = stack.pop()
                neighbors = neighbors_dict[curr_node]
                for neighbor in neighbors:
                    if neighbor not in visited:                        
                        visited.add(neighbor)
                        stack.append(neighbor)
            
        return count        

# @lc code=end

