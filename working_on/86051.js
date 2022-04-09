// 없는 숫자 더하기

function solution(numbers) {
  var answer = 0;
  const ref = [Array(10).keys()];
  var a = ref.filter((x) => !numbers.includes(x));
  a.forEach((element) => {
    answer += element;
  });

  return answer;
}

numbers = [1, 2, 3, 4, 6, 7, 8, 0];
console.log(solution(numbers));
