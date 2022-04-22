# 최소 직사각형
# def solution(sizes):
#     w = []
#     h = []
#     for size in sizes:
#         w.append(size[0])
#         h.append(size[1])

#     mw = max(w)
#     mh = max(h)
#     print(mw, mh)

#     # 작은쪽을 돌리면 된다.

#     if mw < mh:
#         w.remove(mw)
#         mw = max(w)

#     elif mh < mw:
#         h.remove(mh)
#         mh = max(h)

#     print(mw, mh)

#     return mw * mh


# 힌트 참고한 풀이
def solution(sizes):
    width = []
    height = []
    # 큰 값을 가로, 작은 값을 세로로 둔다.
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))

    return max(width) * max(height)


# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]


print(solution(sizes))
