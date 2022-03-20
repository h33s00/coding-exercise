import sys

stack = [] 
# 스택은 리스트에서 왼쪽이 바닥, 오른쪽이 윗부분으로 가정

n = int(sys.stdin.readline()) 
# 백준 시간초과로 인해 인풋을 이렇게 받음 
# n 으로 실행할 명령의 수를 입력받음
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
