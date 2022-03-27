# 신고 결과 받기


def solution(id_list, report, k):
    # 유저 수만큼 답지 초기화
    answer = []
    for i in range(len(id_list)):
        answer.append(0)

    # Remove Duplicates -> 같은 신고는 하나로 간주.
    report = list(dict.fromkeys(report))

    # 신고 누적 횟수를 담은 딕셔너리 만들기
    dic = {}
    for i in range(len(report)):
        if report[i].split()[-1] in dic.keys():
            dic[report[i].split()[-1]] += 1
            # 유저 신고 누적 횟수 증가 (UPDATE)
        else:
            dic[report[i].split()[-1]] = 1
            # 신고를 당한 유저 엔트리 생성 (CREATE)
    # print(dic)

    # 정지먹은 유저들의 이름이 담긴 리스트 만들기
    blacklist = []
    for key, val in dic.items():
        if val >= k:
            blacklist.append(key)
            # 그 value를 가진 key를 블랙리스트에 추가
    # print(blacklist)

    # 정지먹은 유저들을 신고한 유저들에게 이메일 전송!
    for i in range(len(report)):
        if report[i].split()[-1] in blacklist:
            answer[id_list.index(report[i].split()[0])] += 1

    return answer
