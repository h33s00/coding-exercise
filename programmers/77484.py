# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    # 0은 가능성. 나머지 숫자는 확정.
    # 나머지 숫자로 최저 순위 구함.
    # 맞힌 숫자 개수
    match = 0
    # 최저 순위
    worst = 0
    # 최고 순위
    best = 0
    
    # 확정
    for item in lottos:
        if item in win_nums:
            match = match + 1
    # print(match)
    
    # 맞힐 수도 있는 숫자 개수
    pos_match = match + lottos.count(0)
    # print(pos_match)
            
    # 딕셔너리?
    
    # 순위 정하기 - 가능성 포함, 확정
    li = [pos_match, match]
    # print(li)
    answer = []
    
    for item in li:
        if item == 2:
            answer.append(5)
        elif item == 3:
            answer.append(4)
        elif item == 4:
            answer.append(3)
        elif item == 5:
            answer.append(2)
        elif item == 6:
            answer.append(1)
        else:
            answer.append(6)
        
    return answer