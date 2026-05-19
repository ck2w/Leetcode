
# undirected graph G
# DFS - recursive
def connected_components(graph: dict[int, list[int]]) -> int:
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    count = 0
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

# DFS - iterative
def connected_components(graph: dict[int, list[int]]) -> int:
    visited = set()
    num_components = 0

    for node in graph:
        if node not in visited:
            num_components += 1
            # DFS iterative
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    return num_components