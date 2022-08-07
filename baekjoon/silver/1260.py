import sys
from collections import deque


class Graph:
    # 생성자
    def __init__(self, edges, n):
        # 인접 리스트 Initialized
        self.adjList = {}
        for vertex in range(1, n + 1):
            self.adjList[vertex] = []

        # 무향 그래프에 간선을 추가합니다.
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    # 단, 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문!
    def BFS(self, start):
        visited = []
        queue = deque([start])

        for adj in self.adjList.values():
            adj.sort()

        print(self.adjList)

        while queue:
            print("큐: ", queue)
            print("방문기록: ", visited)
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                queue += self.adjList[vertex]

        return visited

    def DFS(self, start):
        visited = []
        stack = [start]

        for adj in self.adjList.values():
            adj.sort(reverse=True)

        print(self.adjList)

        while stack:
            print("스택: ", stack)
            print("방문기록: ", visited)
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack += self.adjList[vertex]

        return visited


def main():
    # 버퍼 입력
    # first_line = sys.stdin.readline().rstrip().split(" ")
    # n, m, start = list(map(int, first_line))
    # edges = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(m)]

    # 파일 입력
    sys.stdin = open("input4.txt", "r")
    n, m, start = list(map(int, sys.stdin.readline().split()))
    lines = sys.stdin.readlines()
    edges = []
    for edge in lines:
        edges.append(list(map(int, edge.rstrip().split(" "))))
        # print(edges)

    graph = Graph(edges, int(n))

    # 출력
    print(*graph.DFS(start))
    print(*graph.BFS(start))


main()
