//  두 정수 사이의 합

function solution(a, b) {
  var answer = 0;
  if (a == b) {
    answer = a;
  } else if (a > b) {
    for (i = b; i <= a; i++) {
      answer += i;
    }
  } else if (a < b) {
    for (i = a; i <= b; i++) {
      answer += i;
    }
  }
  return answer;
}

console.log(solution(5, 3));
