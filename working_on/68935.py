# 3진법 뒤집기


def solution(n):
    tri = ""
    while n != 0:
        print(n % 3)
        tri += str(n % 3)
        n = n // 3

    return int(tri, 3)


a = solution(1)

print(a)
