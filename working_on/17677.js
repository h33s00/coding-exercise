// 뉴스 클러스터링

function solution(str1, str2) {
  const a = cleansing(str1);
  const b = cleansing(str2);

  console.log(a, b);

  if (a.length == 0 && b.length == 0) {
    return Math.floor(1 * 65536);
  }

  let inter = [];

  let a_set = [...new Set(a)];

  console.log("흠", a_set);

  for (item of a_set) {
    if (b.includes(item)) {
      n = Math.min(
        a.filter((x) => x == item).length,
        b.filter((x) => x == item).length
      );
      for (i = 0; i < n; i++) {
        inter.push(item);
      }
    }
  }

  console.log("교집합: ", inter);

  let union = [];

  console.log(a.concat(b));

  let u_set = [...new Set(a.concat(b))];
  console.log("시바", u_set);

  for (item of u_set) {
    n = Math.max(
      a.filter((x) => x == item).length,
      b.filter((x) => x == item).length
    );
    for (i = 0; i < n; i++) {
      union.push(item);
    }
  }

  return Math.floor((inter.length / union.length) * 65536);
}

function cleansing(str) {
  const s = Array.from(str.toUpperCase());
  const alpha = Array.from(Array(26)).map((e, i) => i + 65);
  const alphabet = alpha.map((x) => String.fromCharCode(x));
  //   console.log(alphabet);
  let c = [];
  for (i = 0; i < s.length; i++) {
    let couple = s.slice(i, i + 2);
    // console.log(couple);
    if (couple.length == 2) {
      if (alphabet.includes(couple[0]) && alphabet.includes(couple[1])) {
        c.push(couple[0] + couple[1]);
      }
    }
  }
  return c;
}

str1 = "FRANCE";
str2 = "french";
// console.log(cleansing(str2));
console.log(solution(str1, str2));
