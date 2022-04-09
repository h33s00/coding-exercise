function solution(arr) {
  let result = [];
  arr.forEach((element) => {
    if (result.length == 0) {
      result.push(element);
    } else if (result[result.length - 1] != element) {
      result.push(element);
    }
  });

  return result;
}
