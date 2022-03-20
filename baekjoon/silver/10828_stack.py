import timeit

stack = []
# 스택은 리스트에서 [1, 2] 왼쪽이 바닥, 오른쪽이 윗부분으로 가정

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.remove(stack[-1])

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

# 실행 부분
num_cmd = int(input()) # 실행할 명령의 수를 입력받음
for i in range(num_cmd):
    i_in = input().split()
    # start = timeit.default_timer()
    if i_in[0] == 'push':
        push(i_in[1])
    elif i_in[0] == 'pop':
        pop()
    elif i_in[0] == 'size':
        size()
    elif i_in[0] == 'empty':
        empty()
    elif i_in[0] == 'top':
        top()
    # stop = timeit.default_timer()
    # print(stop - start)
    # else:
    #     print('없는 명령입니다!')
    # print(stack) # 테스트용

