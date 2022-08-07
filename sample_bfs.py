from collections import deque


def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


graph_list = {
    "begin": set([0]),
    0: set([1, 3]),
    1: set([2]),
    2: set([5]),
    3: set([4]),
    4: set([5]),
    5: set([]),
}
print(BFS_with_adj_list(graph_list, "begin"))
