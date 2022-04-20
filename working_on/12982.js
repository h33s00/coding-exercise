// 예산

function solution(d, budget) {
  var answer = 0;
  if (d.reduce((acc, cur) => acc + cur, 0) <= budget) {
    return d.length;
  } else {
    d.sort((a, b) => a - b);
    // console.log(d);
    for (amount of d) {
      //   console.log(budget);
      budget -= amount;
      if (budget < 0) {
        break;
      } else if (budget >= 0) {
        answer++;
      }
    }
    return answer;
  }
}

d = [1, 3, 2, 5, 4];
budget = 9;
// d = [2, 2, 3, 3];
// budget = 10;

a = solution(d, budget);
console.log(a);
