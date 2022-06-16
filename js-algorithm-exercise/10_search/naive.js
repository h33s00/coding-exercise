function naiveStringSearch(s, sub_s) {
  let matchCount = 0;
  for (let i = 0; i < s.length; i++) {
    for (let k = 0; k < sub_s.length; k++) {
      console.log(s[i + k], sub_s[k]);
      if (s[i + k] !== sub_s[k]) {
        break;
      }
      //   끝에 도달하면,
      if (k === sub_s.length - 1) {
        matchCount++;
      }
    }
  }
  return matchCount;
}

console.log(naiveStringSearch("powowow", "wow"));
