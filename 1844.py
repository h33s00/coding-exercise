# # 게임 맵 최단거리

# # 1트
# def BFS(graph, root, target):
#     queue = [root]
#     visited = []
#     depth = 0
#     while queue:
#         depth += 1
#         qsize = len(queue)
#         print("queue:", queue)
#         # print("visited: ", visited)
#         for i in range(qsize):
#             v = queue.pop(0)
#             # 방문한 정점이 타겟이라면 바로 리턴!
#             if v == target:
#                 return depth
#             if v not in visited:
#                 visited.append(v)
#                 queue.extend(graph[v])

#     # 정점을 모두 방문했으나 타겟을 만나지 못하면 여기로 오게된다.
#     return -1


# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])

#     start = str([0, 0])
#     target = str([n - 1, m - 1])

#     # MAKE A GRAPH
#     graph = {}
#     for i in range(n):
#         for k in range(m):
#             if maps[i][k] == 1:
#                 # ADD AS VERTEX
#                 vertex = str([i, k])
#                 graph[vertex] = []

#                 # CHECK RIGHT
#                 if i + 1 < n and maps[i + 1][k] == 1:
#                     graph[vertex].append(str([i + 1, k]))

#                 # CHECK DOWN
#                 if k + 1 < m and maps[i][k + 1] == 1:
#                     graph[vertex].append(str([i, k + 1]))

#                 # CHECK UP
#                 if k - 1 >= 0 and maps[i][k - 1] == 1:
#                     graph[vertex].append(str([i, k - 1]))

#                 # CHECK LEFT
#                 if i - 1 >= 0 and maps[i - 1][k] == 1:
#                     graph[vertex].append(str([i - 1, k]))

#     bfsResult = BFS(graph, start, target)
#     return bfsResult


# 2트

from collections import deque


def solution(maps):
    # MAP IS N X M
    n = len(maps)
    m = len(maps[0])

    start = [0, 0]
    target = [n - 1, m - 1]

    # 가능한 이동
    dist = 0
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])

    while queue:
        # DEPTH INCREASED!
        dist += 1
        q_size = len(queue)
        for i in range(q_size):
            v = queue.popleft()

            if v == target:
                return dist

            for x, y in moves:
                x_move = v[0] + x
                y_move = v[1] + y

                # IF IT IS A VALID MOVE,
                if 0 <= x_move < n and 0 <= y_move < m and maps[x_move][y_move] == 1:
                    # BFS 특성상 방문 표시를 이 시점에서 해줘야합니다!
                    maps[x_move][y_move] = 0
                    # ADD VALID CONNECTION
                    queue.append([x_move, y_move])

    return -1


maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
]

# maps = [
#     [1, 0, 1, 1, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1],
# ]


print(solution(maps))
