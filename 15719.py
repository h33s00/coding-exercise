# 중복된 숫자
import sys

# n = int(input())
# arr = list(map(int, input().split(" ")))
# print(abs(sum(list(map(int, x))) - sum(range(1, int(n)))))

# n = 10
# arr = [1, 2, 2, 5, 6, 4, 3, 7, 8, 9]

N = int(input())
sumN = sum(range(1, int(N)))
numbers = sys.stdin.readline().rstrip()
sumNum = 0
temp = ""
for num in numbers:
    if num.isdigit():
        temp += num
    else:
        sumNum += int(temp)
        temp = ""

# 마지막 숫자의 처리
sumNum += int(temp)

print(sumNum - sumN)
