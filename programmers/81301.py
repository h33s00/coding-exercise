# 숫자 문자열과 영단어

def solution(s):
    answer = ''
    d = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
         'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    # 경우의 수:
    # 문자열과 숫자가 섞여있는 경우, 사이를 끊어준다.
    # - 문자열 문자열 숫자식으로 섞여있는 경우도 있다.
    # 그냥 숫자로만 이루어진 경우 그대로 리턴한다.

    al = []
    bkmk = 0 #인덱싱용 북마크

    for i in range(len(s)):
        # 숫자인 경우
        if s[i] in d.values():
          answer = answer + s[i]
          bkmk = i+1
        # 영단어인 경우
        elif s[bkmk:i+1] in d:
          al.append(s[bkmk:i+1])
          answer = answer + '_'
          bkmk = i+1
    
    for item in al:
      answer = answer.replace('_', d[item], 1) #왼쪽부터 돌아간다.
    
    answer = int(answer)
    return answer