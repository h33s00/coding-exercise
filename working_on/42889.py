# 실패율

def solution(N, stages):
    answer = []
    
    # 초기 유저 수
    user = len(stages)
    # 스테이지 순으로 실패율
    flist = []
    
    for i in range(N): 
        # (1~5까지 스테이지에 대하여)
        # 실패율 계산
        f = stages.count(i+1) / user
        # 실패율 계산 추가
        flist.append(f)
        # 탈락한 유저 제거
        user = user - stages.count(i+1)
    
    for i in range(N):
        # 스테이지 수만큼 돌아가도록 설정!!!
        s = flist.index(max(flist))
        answer.append(s+1)
        flist[s] = -1
        
    return answer