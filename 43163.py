import re

# 정답

import collections


def check_one_dist(s1, s2):
    d = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            d = d + 1
        if d == 2:
            return False
    return True


def solution(begin, target, words):
    visit = collections.deque()
    dist_visit = collections.deque()
    queue = collections.deque()
    dist_queue = collections.deque()

    d = 0
    queue.append(begin)
    dist_queue.append(d)

    while len(queue) != 0:
        node = queue.popleft()
        print(f"노드는 {node}")
        dist = dist_queue.popleft()
        print(f"누적거리는 {dist}")
        visit.append(node)
        dist_visit.append(dist)

        if node == target:
            return dist

        # node에 따라올수 있는 1dist 리스트 추가
        for string in words:
            if (
                (string not in visit)
                and (string not in queue)
                and check_one_dist(node, string)
            ):
                queue.append(string)
                dist_queue.append(dist + 1)

    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)

# print(check_one_dist(begin, "dot"))
