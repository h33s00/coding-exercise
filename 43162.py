# 네트워크
# 임의의 노드에서 DFS 하면 연결된 모든 노드가 담긴다.
# 위는 하나의 네트워크.
# 이 후는 방금 네트워크를 제외한 노드들을 탐색하면 된다.


def solution(n, computers):
    answer = 0

    # 연결고리가 존재하는지 서치할 컴퓨터들
    nodes = list(range(n))

    while nodes:
        node = nodes.pop()
        # 네트워크 = 해당 컴퓨터에 연결된 모든 컴퓨터들의 이름
        network = DFS(n, computers, node)
        answer += 1
        nodes = list(set(nodes) - network)

    return answer


def DFS(n, computers, start):
    stack = [start]
    visited = set()

    while stack:
        i = stack.pop()
        visited.add(i)
        for j in range(n):
            if j not in visited and computers[i][j] == 1:
                stack.append(j)
        print(stack)

    return visited


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
