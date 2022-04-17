//  메뉴 리뉴얼
function solution(orders, course) {
  let answer = [];
  for (i = 0; i < orders.length; i++) {
    for (k = 1; k < orders.length; k++) {
      if (i != k) {
        // let item1 = orders[i].split("");
        item1 = ["A"];
        item2 = ["A", "B"];
        // let item2 = orders[k].split("");
        item2.includes(item1) ? console.log("응!") : console.log("아니!");
      }
    }
  }

  //   orders.forEach((element) => {
  //     if ("AB" in element) {
  //       console.log(element);
  //     }
  //   });

  return answer;
}

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
// orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"];
// orders = ["XYZ", "XWY", "WXA"];
course = [2, 3, 4];
// course = [2, 3, 5];
a = solution(orders, course);
console.log(a);
