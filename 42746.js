// 가장 큰 수

function solution(numbers) {
  let answer = "";
  let snum = numbers.map((x) => x.toString());
  console.log(snum);
  snum.sort((a, b) => {
    if (parseInt(a[0]) > parseInt(b[0])) {
      return 1;
    }
    if (parseInt(a[0]) < parseInt(b[0])) {
      return -1;
    }
    // if (a[0] == b[0]) {
    //   if (a[0] + b.slice(1) > b[0] + a.slice(1)) {
    //     return -1;
    //   }
    //   if (a[0] + b.slice(1) < b[0] + a.slice(1)) {
    //     return 1;
    //   }
    // }
  });
  console.log(snum);

  return answer;
}

numbers = [3, 30, 34, 5, 9]; // "9534330"
console.log(solution(numbers));

a = "3423";
console.log(a.slice(1));
console.log(parseInt(a[0]));
