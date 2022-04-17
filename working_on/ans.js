//  메뉴 리뉴얼 - 자바스크립트 답안
function solution(orders, course) {
  const ordered = {};
  const candidates = {};
  const maxNum = Array(10 + 1).fill(0);
  console.log(maxNum);
  const createSet = (arr, start, len, foods) => {
    if (len === 0) {
      ordered[foods] = (ordered[foods] || 0) + 1;

      // console.log(ordered);

      if (ordered[foods] > 1) candidates[foods] = ordered[foods];

      maxNum[foods.length] = Math.max(maxNum[foods.length], ordered[foods]);

      return;
    }

    for (let i = start; i < arr.length; i++) {
      createSet(arr, i + 1, len - 1, foods + arr[i]);
    }
  };

  orders.forEach((od) => {
    // arr.sort는 기본적으로 사전식 배열
    const sorted = od.split("").sort();

    console.log(sorted);

    // 주문한 음식을 사전순으로 배열해서 문자열을 만든다.
    // course에 있는 길이만 만들면 된다.
    course.forEach((len) => {
      createSet(sorted, 0, len, "");
    });
  });

  const launched = Object.keys(candidates).filter(
    (food) => maxNum[food.length] === candidates[food]
  );

  return launched.sort();
}

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
// orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"];
// orders = ["XYZ", "XWY", "WXA"];
course = [2, 3, 4];
// course = [2, 3, 5];
a = solution(orders, course);
console.log(a);
