# 신규 아이디 추천


def solution(new_id):
    answer = ""
    # ok is a list of possible chrs;
    ok = (
        list(map(chr, range(97, 123)))
        + list([str(x) for x in range(0, 10)])
        + ["-", "_", "."]
    )

    # 1. check if uppercase exists; if so, convert to lowercase;
    answer = str.lower(new_id)
    # print(f'1단계: {answer}')

    # 2. check if any unexpected chr exists; if so remove them;
    for c in answer:
        if c not in ok:
            # print(c)
            answer = answer.replace(c, "", 1)
    # print(f'2단계: {answer}')

    # 3. check if '..' exists; if so remove them;
    while ".." in answer:
        answer = answer.replace("..", ".")
    # print(f'3단계: {answer}')

    # 4. check if first or last index is '.'; if so remove them;
    if len(answer) >= 1 and answer[0] == ".":
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == ".":
        answer = answer[:-1]
    # print(f'4단계: {answer}')

    # 5. check if the id is empty; if so change it to 'a';
    if len(answer) == 0:
        answer = "a"
    # print(f'5단계: {answer}')

    # 6. check if length is longer than 16, if so remove from right.
    if len(answer) >= 16:
        answer = answer[:15]
        # 6-2. if the last one is '.', same as #4
        if answer[-1] == ".":
            answer = answer[:-1]
    # print(f'6단계: {answer}')

    # 7. check if length is less than 2, if so repeat the last letter until it reaches length of 3
    if len(answer) <= 2:
        while len(answer) != 3:
            answer = answer + answer[-1]
    # print(f'7단계: {answer}')

    return answer
