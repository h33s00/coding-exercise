function collectStrings(obj) {
  let arr = [];
  Object.values(obj).forEach((item) => {
    // 오브젝트인 경우
    if (typeof item == "object") {
      arr = arr.concat(collectStrings(item));
    }
    // 문자열인 경우
    if (typeof item == "string") {
      arr.push(item);
    }
  });
  return arr;
}

const obj = {
  stuff: "foo",
  data: {
    val: {
      thing: {
        info: "bar",
        moreInfo: {
          evenMoreInfo: {
            weMadeIt: "baz",
          },
        },
      },
    },
  },
};

console.log(collectStrings(obj)); // ["foo", "bar", "baz"])
