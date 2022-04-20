# 완주하지 못한 선수


def solution(participant, completion):
    answer = ""

    p_record = {}

    for p in participant:
        if p in p_record:
            p_record[p] += 1
        else:
            p_record[p] = 1

    c_record = {}

    for c in completion:
        if c in c_record:
            c_record[c] += 1
        else:
            c_record[c] = 1

    print(p_record)

    print(c_record)

    for p in participant:
        if p not in c_record:
            answer = p
            break
        if p_record[p] != c_record[p]:
            answer = p
            break

    return answer


participant = ["leo", "kiki", "eden"]
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# participant = ["mislav", "stanko", "mislav", "ana"]


completion = ["eden", "kiki"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# completion = ["stanko", "ana", "mislav"]


# participant = ["a", "a", "a", "b", "c"]
# completion = ["a", "a", "b", "c"]

a = solution(participant, completion)
print(a)
