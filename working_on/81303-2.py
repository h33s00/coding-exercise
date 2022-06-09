# 표 편집
# 두번째 시도 - LinkedList
import collections


def solution(n, k, cmd):
    ll = collections.deque()
    for i in range(n):
        ll.append(i)

    answer = ""

    print(ll)

    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# UP, DOWN, CUT, Z
print(solution(n, k, cmd))
