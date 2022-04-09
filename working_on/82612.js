// 부족한 금액 계산하기

function solution(price, money, count) {
  var cost = 0;
  for (let i = 1; i <= count; i++) {
    cost += price * i;
  }
  var answer = money - cost;
  if (answer >= 0) {
    return 0;
  } else {
    return answer * -1;
  }
}

console.log(solution(3, 20, 4));
