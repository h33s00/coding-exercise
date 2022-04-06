// 신고 결과 받기

// 입력 예시
// const id_list = ['muzi','frodo','apeach', 'neo']
// const report = ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi']
// const k = 2

// const id_list = ['con', 'ryan']
// const report = ["ryan con", "ryan con", "ryan con", "ryan con"]
// const k = 3

function solution(id_list, report, k) {
    // 유저 수만큼 답지 초기화
    var answer = [];
    var num_report = [];
    var blacklist = [];

    for (var i = 0; i < id_list.length; i++) {
        answer.push(0);
        num_report.push(0);
    }

    // report 배열에서 중복 요소를 제거
    report = [...new Set(report)]

    // 신고 누적 횟수를 담은 배열 만들기
    report.forEach(function (item) {
        var i = id_list.indexOf(item.split(' ')[1]);
        num_report[i] += 1;
    })
    // console.log(num_report)

    // 정지먹은 유저들의 이름이 담긴 배열 만들기
    num_report.forEach(function (item, index) {
        if (item >= k ) {
            blacklist.push(id_list[index]);
        }
    })
    // console.log(blacklist)

    // 정지먹은 유저들을 신고한 유저들에게 이메일 전송!
    report.forEach(function (item) {
        if (blacklist.includes(item.split(' ')[1])) {
            var bui = id_list.indexOf(item.split(' ')[0])
            answer[bui] += 1;
        }
    })
    // console.log(answer)

    return answer;
}