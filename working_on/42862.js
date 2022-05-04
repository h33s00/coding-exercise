// 체육복

function solution(n, lost, reserve) {
  //  먼저 정렬
  lost.sort();
  reserve.sort();
  let og_lost = [...lost];
  let og_reserve = [...reserve];

  //  도난 당했지만 여벌이 있는 학생은 다른 학생에게 빌려줄수 없다.
  for (student of og_lost) {
    if (og_reserve.includes(student)) {
      reserve.splice(reserve.indexOf(student), 1);
      lost.splice(lost.indexOf(student), 1);
    }
    og_lost = lost;
    og_reserve = reserve;
  }

  //   체육복이 있는 학생 수
  let answer = n - lost.length;

  for (student of lost) {
    if (og_reserve.includes(student - 1)) {
      reserve.splice(reserve.indexOf(student - 1), 1);
      answer += 1;
    } else if (og_reserve.includes(student + 1)) {
      reserve.splice(reserve.indexOf(student + 1), 1);
      answer += 1;
    }
    og_reserve = reserve;
  }

  return answer;
}

// n = 5;
// lost = [2, 4];
// reserve = [2, 9, 1, 3, 5];

// n = 5;
// lost = [2, 4];
// reserve = [3];

// console.log(solution(n, lost, reserve));
// console.log(solution(5, [2, 4, 5], [1, 4]));
console.log(solution(3, [1, 2], [2, 3]));

// # n, lost, reserve = 5, [2, 4], [3]
// # n, lost, reserve = 3, [3], [1]

// # n, lost, reserve = 8, [3, 4, 7], [3, 5]
// # n, lost, reserve = 2, [0], [0]
// # n, lost, reserve = 12, [1, 2, 3, 4, 8, 9, 10, 12], [1]
