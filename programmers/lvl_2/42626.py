# 더 맵게


# 첫번째 풀이 (힙을 사용하지 않은 풀이)
# def solution(scoville, K):
#     answer = 0
#     while True:
#         if min(scoville) >= K:
#             break
#         m = min(scoville)
#         scoville.remove(m)
#         n = min(scoville)
#         scoville.remove(n)
#         scoville.append(m + (n * 2))
#         answer += 1
#         print(scoville)

#     return answer

# 두번째 풀이 (힙 정렬)
import heapq

# https://docs.python.org/ko/3/library/heapq.html


def solution(scoville, K):
    answer = 0
    # 먼저 힙 정렬
    heapq.heapify(scoville)
    # print(scoville)

    while True:
        # 종료 조건
        if scoville[0] >= K:
            break
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        m = heapq.heappop(scoville)
        n = heapq.heappop(scoville)
        heapq.heappush(scoville, m + (n * 2))
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville, k))
