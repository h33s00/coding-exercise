function validAnagram(s1, s2) {
  let s1_obj = {}; // frequency counter
  if (s1.length !== s2.length) return false;
  for (let chr of s1) {
    s1_obj[chr] = (s1_obj[chr] || 0) + 1;
  }
  for (let chr of s2) {
    // if (chr in s1_obj && s1_obj[chr] !== 0) s1_obj[chr] -= 1;
    if (s1_obj[chr]) s1_obj[chr] -= 1;
    else return false;
  }
  return true;
}

console.log(validAnagram("anagram", "nagaram")); // true
