import sys

N = int(sys.stdin.readline())
answer = 0
if N % 3 == 0:
    answer = N // 3
if N % 5 == 0:
    answer = N // 5

cnt = 0
while N > 0:
    if N >= 5:
        N -= 5
        cnt += 1
        print(N)
    elif N >= 3:
        N -= 3
        cnt += 1
        print(N)
    elif N == 0:
        break
    else:
        cnt = -1
        break

if answer == 0 and cnt == -1:
    print(-1)
elif answer == 0 and cnt != -1:
    print(cnt)
elif answer != 0 and cnt == -1:
    print(answer)
elif answer != 0 and cnt != -1:
    print(min(answer, cnt))
