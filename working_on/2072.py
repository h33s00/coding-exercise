tn = int(input())

result = []

# 입력 및 연산
for i in range(tn):
    sum = 0
    t = list(map(int, input().split(" ")))
    for each in t:
        if each % 2 != 0:
            sum += each
    result.append(sum)

# 출력
for i in range(tn):
    print(f"#{i+1} {result[i]}")
