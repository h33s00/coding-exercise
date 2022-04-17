// 문자열 내 마음대로 정렬하기

function solution(strings, n) {
  result = strings.sort((a, b) => {
    if (a.charAt(n) < b.charAt(n)) {
      return -1;
    }
    if (a.charAt(n) > b.charAt(n)) {
      return 1;
    }
    if (a.charAt(n) == b.charAt(n)) {
      if (a < b) {
        return -1;
      }
      if (a > b) {
        return 1;
      }
      return 0;
    }
  });

  //   console.log(result);
  return result;
}

strings = ["abce", "abcd", "cdx"];
// strings = ["sun", "bed", "car"];
n = 1;
a = solution(strings, n);
console.log(a);
