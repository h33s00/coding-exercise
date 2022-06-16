function stringifyNumbers(obj) {
  let n_obj = Object.assign({}, obj);

  Object.keys(obj).forEach((key) => {
    if (typeof obj[key] == "number") {
      n_obj[key] = obj[key].toString();
    }
    // 오브젝트와 배열의 구분 필요 !
    else if (typeof obj[key] == "object" && !Array.isArray(obj[key])) {
      n_obj[key] = stringifyNumbers(obj[key]);
    }
  });

  return n_obj;
}

let obj = {
  num: 1,
  test: [],
  data: {
    val: 4,
    info: {
      isRight: true,
      random: 66,
    },
  },
};

console.log(stringifyNumbers(obj));

/*
{
    num: "1",
    test: [],
    data: {
        val: "4",
        info: {
            isRight: true,
            random: "66"
        }
    }
}
*/
