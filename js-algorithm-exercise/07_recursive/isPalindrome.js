// isPalindrome('awesome') // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
// isPalindrome('amanaplanacanalpanama') // true
// isPalindrome('amanaplanacanalpandemonium') // false

// HELPER FUNCTION

function isPalindrome(word) {
  function reverse(s) {
    if (s.length === 0) return s;
    return s.slice(-1) + reverse(s.slice(0, -1));
  }

  return word == reverse(word) ? true : false;
}

// PURE RECURSION

function isPalindrome(word) {
  //   종료 조건
  if (word.length == 0) {
    return true;
  }
  //   맨앞과 맨뒤의 비교
  if (word[0] == word.slice(-1)) {
    return isPalindrome(word.slice(1, -1));
  } else {
    return false;
  }
}

console.log(isPalindrome("tacocat"));
console.log(isPalindrome("heesoo"));

// t/a/c/o/c/a/t
// 0 1 2 3 4 5 6
// length = 7

// console.log(false + false + false);
