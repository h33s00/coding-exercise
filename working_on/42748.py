# K번째 수


def solution(array, commands):
    answer = []
    for each in commands:
        # 인덱싱을 위해 1씩 빼준다
        i = each[0] - 1
        j = each[1]
        k = each[2] - 1

        answer.append((sorted(array[i:j])[k]))

    return answer


# i부터 j까지 자른 뒤 k번째 수 구하기
# command = [i,j,k]
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 내장함수 쓰지않고 정렬 해보자...
